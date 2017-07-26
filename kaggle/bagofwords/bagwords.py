import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import numpy as np
path = "F:/codeGitBook/kaggle/bagofwords/"
train = pd.read_csv(path+"labeledTrainData.tsv",header=0,delimiter="\t",quoting=3)
print(train)
print(train.shape)
# print(train.columns.values)
# data = train["review"][0]
# example = BeautifulSoup(data,"lxml")
# print(example.get_text())
# letter_only = re.sub("[^a-zA-Z]"," ",example.get_text())
# print(letter_only)
# lower_case = letter_only.lower()
# words = lower_case.split()
# print(words)
# print(stopwords.words("english"))
# words = [w for w in words if not w in stopwords.words("english")]
# print(words)
def review_words(raw_words):
	temp = BeautifulSoup(raw_words,"lxml")
	letter_only = re.sub("[^a-zA-Z]"," ",temp.get_text())
	lower_case = letter_only.lower()
	words = lower_case.split()
	words = [w for w in words if not w in stopwords.words("english")]
	return (" ".join(words))
data = train["review"][0]
print(review_words(data))

clean_train = []
count = 0
for data in train["review"]:
	if (count+1)%1000 == 0:
		print(count)
	count = count + 1
	clean_train.append(review_words(data))
# print(clean_train)

vectorizer  = CountVectorizer(analyzer = "word",\
	                         tokenizer = None, \
	                         preprocessor = None,\
	                         stop_words = None,\
	                         max_features = 5000)

train_data_features = vectorizer.fit_transform(clean_train)
train_data_features = train_data_features.toarray()
# print(train_data_features.shape)
vocab = vectorizer.get_feature_names()
# print(vocab)
dist = np.sum(train_data_features,axis=0)
# for tag,count in zip(vocab,dist):
# 	print(count,tag)

forest = RandomForestClassifier(n_estimators = 100)
forest = forest.fit(train_data_features,train["sentiment"])


test = pd.read_csv(path + "testData.tsv",header=0,delimiter="\t",quoting=3)
# print(test)
# print(test.shape)
num_review = len(test["review"])
clean_test_reviews = []

for i in range(num_review):
	clean_review = review_words(test['review'][i])
	# print(clean_review)
	clean_test_reviews.append(clean_review)

test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()
result = forest.predict(test_data_features)
output = pd.DataFrame(data={"id":test["id"],"senntiment":result})
output.to_csv(path+"bagofwords.csv",index=False,quoting=3)
# print(clean_test_reviews)
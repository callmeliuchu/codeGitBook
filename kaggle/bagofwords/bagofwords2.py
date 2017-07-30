import pandas as pd
from bs4 import BeautifulSoup 
import nltk.data
import re
import logging
from gensim.models import word2vec
path = "F:/codeGitBook/kaggle/bagofwords/"
train = pd.read_csv(path+"labeledTrainData.tsv",
	    header=0,delimiter="\t",quoting=3)
test = pd.read_csv(path+"testData.tsv",
	    header=0,delimiter="\t",quoting=3)
unlabeled_train = pd.read_csv(path+"unlabeledTrainData.tsv",
	    header=0,delimiter="\t",quoting=3)
# print(train)
# print(test)
# print(unlabeled_train)
print(train["review"].size,test["review"].size,unlabeled_train["review"].size)
def review_wordlist(raw_words,remove_stopwords=False):
	temp = BeautifulSoup(raw_words,"lxml")
	letter_only = re.sub("[^a-zA-Z]"," ",temp.get_text())
	lower_case = letter_only.lower()
	words = lower_case.split()
	if remove_stopwords:
		words = [w for w in words if not w in stopwords.words("english")]
	return (words)

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
# words = train["review"][0]
# print(words)
# sen = tokenizer.tokenize(words.strip())
# print(sen)
def review_to_sentences(review,tokenizer,remove_stopwords=False):
	raw_sentences = tokenizer.tokenize(review.strip())
	sentences = []
	for raw_sentence in raw_sentences:
		if len(raw_sentence)>0:
			sentences.append(review_wordlist(raw_sentence,remove_stopwords))
	return sentences


sentences = ["a","hello"]
# for review in train["review"]:
# 	sentences = sentences + review_to_sentences(review,tokenizer)

# for review in unlabeled_train["review"]:
# 	sentences = sentences + review_to_sentences(review,tokenizer)

# print(sentences)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',\
	level=logging.INFO)
num_features = 300
min_word_count = 40
num_works = 4
context = 10
downsampling = 1e-3
model = word2vec.Word2Vec(sentences, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)




from sklearn.feature_extraction.text import CountVectorizer
import os
# vectorizer = CountVectorizer(min_df=1)
# print(vectorizer)
# content = ["how to format my hard disk","hard disk format problems"]
# x = vectorizer.fit_transform(content)
# print(content)
# print(vectorizer.get_feature_names())
# print(x.toarray())

def read_txt():
	file = "toy"
	for file_root,f1,file_names in os.walk(file):
		for file_name in file_names:
			file_path = os.path.join(file_root,file_name)
			# print(file_path)
			with open(file_path,'r') as f:
				print(f.read())

read_txt()
DIR = "toy"
posts = [open(os.path.join(DIR,f)).read() for f in os.listdir(DIR)]
print(posts)
vectorizer = CountVectorizer(min_df=1)
x = vectorizer.fit_transform(posts)
num_samples,num_features = x.shape
print(num_samples,num_features)
print(x)
print(vectorizer.get_feature_names())
# new_post = "imaging databases"
# new_post_vec = vectorizer.transform([new_post])
# print(new_post_vec.toarray())
# import scipy as sp                                    
# print(sp.linalg.norm([3,4]))
# vectorizer = CountVectorizer(min_df=1,stop_words="english")
# print(sorted(vectorizer.get_stop_words())[0:20])
import nltk.stem
s = nltk.stem.SnowballStemmer('english')
val = s.stem("graphics")
print(val)
val1 = s.stem("imaging")
print(val1)
val3 = s.stem("imagination")
print(val3)
val4 = s.stem("imagine")
print(val4)
val5 = s.stem("buys")
print(val5)
val6 = s.stem("buying")
print(val6)
val7 = s.stem("bought")
print(val7)
class StemmedCountVectorizer(CountVectorizer):
	def build_analyzer(self):
		analyzer = super(StemmedCountVectorizer,self).build_analyzer()
		return lambda doc: (s.stem(w) for w in analyzer(doc))
stemVectorizer = StemmedCountVectorizer(min_df=1,stop_words="english")
stemVectorizer.fit_transform(posts)
print(stemVectorizer.get_feature_names())
import math
def tfidf(term,doc,docset):
	tf = float(doc.count(term))/sum(doc.count(w) for w in set(doc))
	idf = math.log(float(len(docset))/(len([doc for doc in docset if term in doc])))
	return tf*idf
# a,abb,abc=['a'],['a','b','b'],['a','b','c']
# D = [a,abb,abc]
# print(tfidf('a',a,D))
# s = sum(a.count(w) for w in D)
# print(s)

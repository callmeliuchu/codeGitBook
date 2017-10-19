from sklearn.feature_extraction.text import CountVectorizer
import os
import scipy as sp
import sys
import nltk.stem
import math
english_stemmer = nltk.stem.SnowballStemmer('english')
vectorizer = CountVectorizer(min_df = 1,stop_words='english')
# print(sorted(vectorizer.get_stop_words())[0:20])
# print(vectorizer)
# content = ["how to format my hard disk","hard disk format problems"]
# X = vectorizer.fit_transform(content)
# print(vectorizer.get_feature_names())
# print(X.toarray().transpose())

def dis_raw(v1,v2):
	arr = v1 - v2
	return sp.linalg.norm(arr.toarray())

def read_data(file_path):
	posts = [open(os.path.join(file_path,file)).read() for file in os.listdir(file_path)]
	return posts

def nearest(train_data,post,post_contents,dis_raw=dis_raw):
	num_samples,num_features=train_data.shape
	best_dist = sp.inf
	best_doc = None
	best_i = None
	for i in range(0,num_samples):
		post_str = post_contents[i]
		post_vec = train_data.getrow(i)
		dis = dis_raw(post_vec,post)
		print("post %i dist %.2f  posts:%s"%(i,dis,post_str))
		if dis<best_dist:
			best_dist = dis
			best_i = i
			best_doc = post_str
	print("best num:%i ,dis:%.2f best doc:%s"%(best_i,best_dist,best_doc))


def dist_norm(v1,v2):
	v1_normalize = v1/sp.linalg.norm(v1.toarray())
	v2_normalize = v2/sp.linalg.norm(v2.toarray())
	delta = v1_normalize - v2_normalize
	return sp.linalg.norm(delta.toarray())

class StemmedCountVectorizerizer(CountVectorizer):
	def build_analyzer(self):
		analyzer = super(StemmedCountVectorizerizer,self).build_analyzer()
		return lambda doc:(english_stemmer.stemmer.stem(w) for w in analyzer(doc))


def tfidf(term,doc,docset):
	tf = float(doc.count(term))/sum([doc.count(term) for doc in docset])
	idf = math.log(float(len(docset))/(len([doc for doc in docset if term in doc])))
	return tf*idf

vectorizer = StemmedCountVectorizerizer(min_df=1,stop_words='english')
print(vectorizer)



posts = read_data('data')
x_train = vectorizer.fit_transform(posts)
print(x_train)
num_samples,num_features = x_train.shape
print(num_samples,num_features)
print(vectorizer.get_feature_names())
new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print(new_post_vec)
print(new_post_vec.toarray())
nearest(x_train,new_post_vec,posts,dist_norm)
a,abb,abc = ["a"],["a","b","b"],['a','b','c']
D = [a,abb,abc]
print(tfidf("a",a,D))
print(tfidf("b",abb,D))
print(tfidf("a",abc,D))
print(tfidf("b",abc,D))
print(tfidf("c",abc,D))
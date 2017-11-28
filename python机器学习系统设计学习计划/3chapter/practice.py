from sklearn.feature_extraction.text import CountVectorizer
import os
import scipy as sp
import sys
import nltk.stem
import math
from sklearn.feature_extraction.text import TfidfVectorizer
english_stemmer = nltk.stem.SnowballStemmer('english')
print('begin')
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


class StemmedTfidfVectorizer(TfidfVectorizer):
	def build_analyzer(self):
		analyzer = super(TfidfVectorizer,self).build_analyzer()
		return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = CountVectorizer(min_df = 1,stop_words='english',decode_error='ignore')
vectorizer = StemmedCountVectorizerizer(min_df=1,stop_words='english',decode_error='ignore')
vectorizer = StemmedTfidfVectorizer(min_df=1,stop_words='english',decode_error='ignore')
# print(vectorizer)
print('begin')


# posts = read_data('data')
# x_train = vectorizer.fit_transform(posts)
# print(x_train)
# num_samples,num_features = x_train.shape
# print(num_samples,num_features)
# print(vectorizer.get_feature_names())
# new_post = "imaging databases"
# new_post_vec = vectorizer.transform([new_post])
# print(new_post_vec)
# print(new_post_vec.toarray())
# nearest(x_train,new_post_vec,posts,dist_norm)
# a,abb,abc = ["a"],["a","b","b"],['a','b','c']
# D = [a,abb,abc]
# print(tfidf("a",a,D))
# print(tfidf("b",abb,D))
# print(tfidf("a",abc,D))
# print(tfidf("b",abc,D))
# print(tfidf("c",abc,D))
import sklearn.datasets
MILCOMP_DIR = r"F:\python机器学习系统设计\1400OS_03_Codes\1400OS_03_Codes\dataset-379-20news-18828_YRKSU"
data = sklearn.datasets.load_mlcomp("20news-18828",mlcomp_root=MILCOMP_DIR)
print('begin')
# print(data.filenames)
# print(len(data.filenames))
# print(data.target_names)
train_data = sklearn.datasets.load_mlcomp("20news-18828","train",mlcomp_root=MILCOMP_DIR)
print(len(train_data.filenames))
test_data = sklearn.datasets.load_mlcomp("20news-18828","test",mlcomp_root=MILCOMP_DIR)
print(len(test_data.filenames))
groups = [
    'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
    'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
dataset = sklearn.datasets.load_mlcomp("20news-18828","train",mlcomp_root=MILCOMP_DIR,categories=groups)
vectorizer = StemmedTfidfVectorizer(min_df=10,max_df=0.5,stop_words='english',decode_error='ignore')
vectorized = vectorizer.fit_transform(dataset.data)
num_samples,num_features = vectorized.shape
print(num_samples,num_features)

num_clusters = 50
from sklearn.cluster import KMeans
km = KMeans(n_clusters=num_clusters,init='random',n_init=1,verbose=1)
km.fit(vectorized)
print(km.labels_.shape)

new_post = \
    """Disk drive problems. Hi, I have a problem with my hard disk.
After 1 year it is working only sporadically now.
I tried to format it, but now it doesn't boot any more.
Any ideas? Thanks.
"""
new_post_vec = vectorizer.transform([new_post])
print(new_post_vec)
new_post_label = km.predict(new_post_vec)[0]
print(new_post_label)
similar_indices = (km.labels_==new_post_label).nonzero()[0]
print(similar_indices)


similar = []
for i in similar_indices:
	dist = sp.linalg.norm((new_post_vec-vectorized[i]).toarray())
	similar.append((dist,dataset.data[i]))
similar = sorted(similar)
print(len(similar))
show_at_1 = similar[0]
show_at_2 = similar[len(similar)//2]
show_at_3 = similar[-1]

print(show_at_1)
print(show_at_2)
print(show_at_3) 

post_group = zip(dataset.data,dataset.target)
z = [(len(post[0]),post[0],dataset.target_names[post[1]] )for post in post_group]
print(sorted(z)[5:7])
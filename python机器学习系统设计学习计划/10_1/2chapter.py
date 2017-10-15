from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
import random

def distance(p1,p2):
	return np.sum((p1-p2)**2)


def knn(data_set,vec,labels):
	dis_arr = np.array([distance(exc,vec) for exc in data_set])
	min_arg = dis_arr.argmin()
	return labels[min_arg]


data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
print(target)
vec1 = features[0]
new_data_set = features[10:]
new_labels = target[10:]
for i in range(10):
	veci = features[i]
	true_label = target[i]
	result_label = knn(new_data_set,veci,new_labels)
	print(result_label,result_label)




# print(data)
# arr = [target == 1,0]
# print(target)
# print(features[:,0])
# print(features[:,1])
# for t,marker,c in zip(range(3),">ox","rgb"):
# 	plt.scatter(features[target == t,0],
# 				features[target == t,1],
# 				marker=marker,
# 				c = c)
# plt.show()
#获取数据
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np


#加载数据
data = load_iris()
features = data['data']
feature_names = data['target_names']
target = data['target']
print(features[target==2][:,3])


def draw_pic():
	# print(data)
	# #获取每一个属性
	# print(features,feature_names,target)
	# print(len(features))
	for t,marker,c in zip(range(3),"o>x","rgb"):
		# print(features[target==t,0])
		plt.scatter(features[target==t,0],
			features[target==t,1],
			marker = marker,
			c=c)
	plt.show()

# print(data)
# print(features)
plength = features[:,2]
# print(plength)
is_setosa = (target == 0)
# print(is_setosa)
# print(~is_setosa)
max_is_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
# print(max_is_setosa,min_non_setosa)

labels = data['target_names'][target]
# print(labels)
features = features[~is_setosa]
# print(non_setosa_features)
labels = labels[~is_setosa]
# print(non_setosa_labels)
virginica = (labels  == 'virginica')
# print(virginica)


def learn_model(features,models):
	best_acc = -1.0
	for fi in range(features.shape[1]):
		thresh = features[:,fi].copy()
		thresh.sort()
		for t in thresh:
			pred = (features[:,fi] > t)
			acc = (pred == models).mean()
			if acc > best_acc:
				best_acc = acc
				best_fi = fi
				best_t = t
	return best_fi,best_t

print(learn_model(features,virginica))

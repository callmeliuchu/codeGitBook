import csv 
import numpy as np
from collections import Counter
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

def get_pic():
	digit_pic = {}
	with open('train.csv',encoding='utf-8') as f:
		csv_reader = csv.reader(f)
		lines = list(csv_reader)
		for i in range(1,len(lines)):
			line = lines[i]
			num = int(line[0])
			newline = line[1:]
			s = ""
			for j in range(28):
				s = s + "\t".join(newline[j*28:(j+1)*28]) + "\n"
			digit_pic[i] =(num,s) 

def convertopic(line):
	s = ""
	for j in range(28):
		s = s + "\t".join(line[j*28:(j+1)*28]) + "\n"
	return s




def convert(num):
	anum = int(num)
	if anum!=0:
		anum=1
	return anum




def loadDataSet(path,kind='train'):
	data = []
	labels = []
	with open(path,encoding='utf8') as f:
		csv_reader = csv.reader(f)
		lines = list(csv_reader)
		for i in range(1,len(lines)):
			line = lines[i]
			if kind == 'train':
				label = int(line[0])
				vec = line[1:]
				labels.append(label)
			else:
				vec = line
				labels.append(convertopic(vec))
			data.append(list(map(lambda x:convert(x),vec)))
	return np.array(data),labels




def knn(train_data,vec,labels,k=3):
	new_data = train_data - vec
	new_data = new_data**2
	new_arr =  new_data.sum(axis=1)
	new_arr = new_arr**0.5
	index_arr = new_arr.argsort()
	counts = {}
	for i in range(k):
		index = index_arr[i]
		label = labels[index]
		if label not in counts:
			counts[label] = 0
		counts[label] = counts[label] + 1
	return max(Counter(counts))
	




# print(train_data)
# print(test_data)
# knn(train_data,train_data[0],train_labels,4)
def test():
	train_data,train_labels = loadDataSet('train.csv','train')
	test_data,pic_arr= loadDataSet('test.csv','test')
	pred = []
	for i in range(len(test_data)):
		test_vec = test_data[i]
		label = knn(train_data,test_vec,train_labels,4)
		pred.append(label)
	submission = pd.DataFrame({
	        "ImageId": list(range(1,len(pred)+1)),
	        "Label": pred
	    })
	submission.to_csv('submission_1.csv',index=False)

# test()
# train_data,train_labels = loadDataSet('train.csv','train')
# data = train_data[0].reshape(28,28)
# new_im = Image.fromarray(data)
# plt.imshow(data)
# new_im.show()
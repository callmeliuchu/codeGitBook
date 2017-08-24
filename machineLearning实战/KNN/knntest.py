import numpy as np
from collections import Counter
import random as rnd
import os
import pandas as pd



def loadDataSet():
	path = 'datingTestSet.txt'
	dataMat = []
	labels = []
	with open(path) as f:
		lines = f.readlines()
		arrlines = list(map(lambda x:x.strip().split(),lines))
		for arrline in arrlines:
			labels.append(arrline[-1])
			vec = arrline[:-1]
			vec = list(map(lambda x:float(x),vec))
			dataMat.append(vec)
	return np.array(dataMat),labels


def normalize(dataMat):
	maxarr = dataMat.max(axis=0)
	minarr = dataMat.min(axis=0)
	rangearr = maxarr - minarr
	dataMat = (dataMat - minarr)/rangearr
	return dataMat,minarr

def knn(trainData,vec,labels,k=3):
	newMat = trainData - vec
	newMat = newMat**2
	newArr = newMat.sum(axis=1)
	newArr = newArr**0.2
	indexArr = newArr.argsort()
	labelsArr = list(map(lambda x:labels[x],indexArr))
	return max(Counter(labelsArr[:k]))


def genTestData(dataMat,labels,h = 0.1):
	m,n = dataMat.shape
	test_num = int(h*m)
	train_num = m - test_num
	return dataMat[:test_num],labels[:test_num],dataMat[test_num:],labels[test_num:]
	

def test():
	dataMat,labels = loadDataSet()
	dataMat,minArr= normalize(dataMat)
	test_data,test_lables,train_data,train_labels= genTestData(dataMat,labels,0.5)
	index = 0
	e = 0.0
	for test_vec in test_data:
		label = knn(train_data,test_vec,train_labels,5)
		true_label = test_lables[index]
		index = index + 1
		if(label!=true_label):
			e = e + 1
			print(label,true_label)
	print(e/len(test_lables))


def readDights(path):
	vec = []
	with open(path) as f:
		lines = f.readlines()
		for line in lines:
			arr = list(map(lambda x:int(x),line.strip()))
			vec.extend(arr)
	return vec


def loadDigits(filepath):
	filelist = os.listdir(filepath)
	train_data = []
	train_labels = []
	for filename in filelist:
		label = int(filename.split('_')[0])
		path = filepath + "/" +filename
		vec = readDights(path)
		train_data.append(vec)
		train_labels.append(label)
	return np.array(train_data),train_labels


def digitsTest():
	train_data,train_labels=loadDigits('trainingDigits')
	test_data,test_labels=loadDigits('testDigits')
	# print(train_data,train_labels)
	# print(test_data,test_labels)
	index = 0
	e = 0.0
	for vec in test_data:
		label = knn(train_data,vec,train_labels,3)
		true_label = test_labels[index]
		index = index + 1
		if label != true_label:
			e = e + 1
		else:
			print(label,true_label)
	print(e/len(test_data))


df = pd.read_csv('train.csv',header=None)
print(df[,:])




# digitsTest()

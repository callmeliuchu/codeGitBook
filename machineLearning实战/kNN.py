from numpy import *
import operator

def loadDataSet():
	#自定义简单小数据用于测试
	dataArr = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify(vecInput,dataSet,labels,k):
	#tempData是向量之间的差，维数不一致会进行广播达到一致
	tempData = dataSet - vecInput
	#欧氏距离计算
	tempData=tempData**2
	dis = tempData.sum(axis=1)
	dis = dis**0.5
	#按照距离排序，输出索引
	sortedDistIndices = dis.argsort()
	#统计向量vecInput距离dataSet最近的k个标签
	classCount = {}
	for i in range(k):
		index = sortedDistIndices[i]
		label = labels[index]
		if label in classCount:
			classCount[label]=classCount[label]+1
		else:
			classCount[label]=0
	#对收集的数据排序取首位
	sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]





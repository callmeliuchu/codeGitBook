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


def file2matrix(fileName):
	#读取每一行
	lines = open(fileName).readlines()
	#记录每一行的数值
	returnMat = []
	#得到每一行最后一个label
	labels = []
	for line in lines:
		data = line.strip().split('\t')
		numArr = [float(num) for num in data[:-1]]
		labels.append(data[-1])
		returnMat.append(numArr)
	#返回数据
	return array(returnMat),labels

def testDataSet():
	#测试数据
	fileName =  'F:\python\machinelearning\machinelearninginaction-master\Ch02/datingTestSet.txt'
	return file2matrix(fileName)

def autoNorm(dataSet):
	#得到每一列的最小值
	minArr = dataSet.min(0)
	#得到每一列的最大值
	maxArr = dataSet.max(0)
	#取得范围
	rangeArr = maxArr - minArr
	#广播，normalize 数据
	returnMat = (dataSet-minArr)/rangeArr
	return returnMat,rangeArr,minArr

def datingClassTest():
	h = 0.10
	dataSet,labels = testDataSet()
	normalMat,rangeArr,minArr=autoNorm(dataSet)
	m = shape(dataSet)[0]
	num = int(h*m)
	e = 0.0
	for i in range(num):
		label = classify(normalMat[i,:],normalMat[num:m,:],labels,3)
		if labels[i]!=label:
			e = e + 1.0
		else:
			print('data:',labels[i],'predicted:',label)
	return e/float(m)







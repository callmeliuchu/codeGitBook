import numpy as np


def loadDataSet(fileName):
	#打开数据
	file = open(fileName)
	returnMat = []
	lines =  file.readlines()
	for line in lines:
		data = line.strip().split('\t')
		vec = [float(num) for num in data]
		returnMat.append(vec)
	return np.array(returnMat)


def testData():
	#测试数据
	path = 'F:\python\machinelearning\machinelearninginaction-master\Ch10/testSet.txt'
	dataSet = loadDataSet(path)
	return dataSet


def randCent(dataSet,k):
	m,n=np.shape(dataSet)
	maxArr = dataSet.max(axis=0)
	minArr = dataSet.min(axis=0)
	rangArr = maxArr - minArr
	returnMat = []
	for i in range(k):
		vec = []
		for j in range(n):
			val = float(np.random.random()*rangArr[j])
			vec.append(val)
		returnMat.append(vec)
	return np.array(returnMat)

def disEclud(vecA,vecB):
	#计算距离
	dis = np.sqrt(np.sum(np.power(vecA - vecB,2)))
	return dis


def kmeans(dataSet,k,dis=disEclud,createCent=randCent):
	m = np.shape(dataSet)[0]
	cent = createCent(dataSet,k)
	print(cent)
	#cluster记录的是标记为某一个cent和到它的距离比如0，12
	cluster = np.mat(np.zeros((m,2)))
	#设置一个Flag来判断质点有没有改变，一旦改变继续循环
	isChange = True
	while isChange:
		isChange = False
		for i in range(m):
			minDis = np.inf
			loc = -1
			for j in range(k):
				aDis = dis(dataSet[i],cent[j])
				if minDis > aDis:
					minDis = aDis
					loc = j
			if cluster[i,0]!=loc:
				isChange = True
			cluster[i,:]=loc,minDis**2
		#print(cent)
		for j in range(k):
			#print(cluster)
			#print('..............')
			#print(np.nonzero(cluster[:,0].A==j)[0])
			newCluster = dataSet[np.nonzero(cluster[:,0].A==j)[0]]
			#print(newCluster)
			#print('----------')
			#print(newCluster)
			#print('--------------------')
			#print(newCluster)
			#print(np.mean(newCluster,axis=0))
			cent[j,:]=np.mean(newCluster,axis=0)
			#print(amean)
	return cent,cluster
		







if __name__ == '__main__':
	dataSet = testData()
	#cent=randCent(dataSet,3)
	#print(cent)
	cent,cluster=kmeans(dataSet,3)
	#print(cent)
	


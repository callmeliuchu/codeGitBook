import os
import numpy as np
foldpath = "./data"

class analysis():
	def __init__(self,filename):
		self.datapath = os.path.join(foldpath,filename)
		self.data = self.readData()
		self.aver = self.averge()
		self.subAver = self.subAv()
		self.cov = self.coveriable()
		self.feaVec = self.convFeaVec()
		self.feaVects = self.getFeatVects()
		self.topKVec = self.getTopKVec()
		self.newArr = self.dealArr()


	def readData(self):
		data = []
		with open(self.datapath) as f:
			lines = f.readlines()
			for line in lines:
				arr = line.strip().split()
				data.append([float(num) for num  in arr])
		return np.array(data)

	def averge(self):
		m,n=np.shape(self.data)
		sumarr = self.data.sum(axis=0)
		return sumarr/m

	def subAv(self):
		return self.data - self.aver

	def coveriable(self):
		m,n=np.shape(self.subAver)
		return np.dot(self.subAver.T,self.subAver)/(m-1)
	
	def convFeaVec(self):
		return np.linalg.eig(self.cov)

	def getFeatVects(self):
		arr1,arr2=self.feaVec
		return arr2

	def getTopKVec(self,k=2):
		arr1,arr2=self.feaVec
		return arr2.T[:k]

	def dealArr(self):
		return np.dot(self.data,self.feaVects)

	def getNewArr(self):
		return self.newArr



arr = analysis("data.txt").getNewArr()
print(arr)


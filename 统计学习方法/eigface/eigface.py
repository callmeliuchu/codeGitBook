import numpy as np
from PIL import Image
import os



def get_data():
	with open('test.txt') as f:
		data_set = []
		for line in f.readlines():
			vec = [float(num) for num in line.strip().split('    ')]
			data_set.append(vec)
	return np.array(data_set)

# data = get_data()
# print(data)

class PCA:
	def __init__(self,data_set,k=2):
		self.data_set = data_set


	def data_process(self,k):
		average = self.data_set.sum(axis=0)/float(len(self.data_set))
		subtraction = self.data_set - average
		multi = np.dot(subtraction.T,subtraction)/float(len(self.data_set)-1)
		t,arr= np.linalg.eig(multi)
		# print(average)
		# print(subtraction.T)
		print(arr)
		print(arr[:,0:k])
		sub = arr[:,0:k]
		res = np.dot(self.data_set,sub)
		print(res)

	def test(self):
		self.data_process(2)


# data = get_data()
# process = PCA(data)
# process.test()
# vec = [float(num) for line.strip().split()]


def ImageToMatrix(file):
	file_names = os.listdir(file)
	print(file_names)
	for name in file_names:
		if name.endswith('jpg'):
			path = os.path.join(file,name)
			im = Image.open(path)
			w,h = im.size
			im = im.convert("L")
			data = im.getdata()
			data = np.array(data)
			print(data)


class PCAFace:
	def __init__(self,file):
		self.data_set = []
		self.parse_data_set(file)
		self.data_process()
		print(self.feature)
		print(self.feature_arr)
		# print(self.feature_arr)



	def parse_data_set(self,file):
		file_names = os.listdir(file)
		for name in file_names:
			if name.endswith('jpg'):
				path = os.path.join(file,name)
				im = Image.open(path)
				w,h = im.size
				im = im.convert("L")
				data = im.getdata()
				self.data_set.append(list(data))
		self.data_set = np.array(self.data_set)		


	def data_process(self):
		average = self.data_set.sum(axis=0)/float(len(self.data_set))
		subtraction = self.data_set - average
		multi = np.dot(subtraction,subtraction.T)/float(np.shape((self.data_set))[1]-1)
		# print(multi)
		self.feature,self.feature_arr= np.linalg.eig(multi)

pca = PCAFace('training')
# print(os.listdir('training'))
# ImageToMatrix('training')


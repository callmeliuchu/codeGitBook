import random
import numpy as np

class KmeansTool:
	def __init__(self,path,k=3):
		self.dataSet = None
		self.init_data(path)
		self.k_cluster = k
		self.split_data()

	def init_data(self,path):
		data = []
		with open(path) as f:
			lines = f.readlines()
			for line in lines:
				arr = line.strip().split('\t')
				data.append([float(num) for num in arr])
			f.close()
		self.dataSet = np.array(data)

	def distance(self,vec1,vec2):
		return sum((vec1-vec2)**2)**0.5

	def split_data(self):
		n_deminision = len(self.dataSet[0])
		range_arr = []
		for d in range(n_deminision):
			max_num = max(vec[d] for vec in self.dataSet)
			min_num = min(vec[d] for vec in self.dataSet)
			range_arr.append((min_num,max_num))
		k_arr = []
		for i in range(self.k_cluster):
			vec = []
			for d in range(n_deminision):
				vec.append(random.uniform(range_arr[d][0],range_arr[d][1]))
			k_arr.append(vec)
		k_arr = np.array(k_arr)
		# print(max_num,min_num)
		count = 0
		while count<100:
			table = {}
			flag = True
			for vec in self.dataSet:
				min_dis = float('inf')
				target = -1
				for tag in range(len(k_arr)):
					dis = self.distance(vec,k_arr[tag])
					if min_dis > dis:
						min_dis = dis
						target = tag
				if target not in table:
					table[target] = []
				table[target].append(vec)
			for key,vec in table.items():
				k_arr[key] = sum(vec)/len(vec)
			# print(k_arr)
			count = count + 1
		self.split_k_cluster = k_arr

	def get_k_cluster(self):
		return self.split_k_cluster

	def get_data(self):
		return self.dataSet


path = 'testSet.txt'
tool = KmeansTool(path)
# print(tool.get_data())
print(tool.get_k_cluster())
import numpy as np

def load_data_1():
	data_set = [ [1,1,'yes'],
	             [1,1,'yes'],
	             [1,0,'no'],
	             [0,1,'no'],
	             [0,1,'no']]
	return data_set


def load_data(file_path):
	ret_data = []
	with open(file_path) as f:
		for line in f.readlines():
			data = line.split()
			ret_data.append([float(num) for num in data])
		f.close()
	return  ret_data


# data = load_data_1()
# data = np.mat(data)
# print(data)
# print(np.mean(data[:,0]))



file_path = 'data/ex00.txt'
data = load_data(file_path)
data = np.mat(data)
print(np.mean(data[:,-1]))
# print(data)
# print(data[:,-1])
# print(data[:,-1].T.tolist()[0])
# print(data[:,-1])
# print(np.var(data[:,-1]))
# arr = np.nonzero(data[:,1]>0.0)
# print(data[arr,:])


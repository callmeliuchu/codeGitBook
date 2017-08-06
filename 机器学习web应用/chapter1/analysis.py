import numpy as np
import time
def sum_trad():
	start = time.time()
	x = range(10000000)
	y = range(10000000)
	z = []
	for i in range(len(x)):
		z = x[i] + y[i]
	end = time.time()
	print("trd time: ",(end-start))


def numpy_time():
	start = time.time()
	x = np.arange(10000000)
	y = np.arange(10000000)
	z = x+ y
	end = time.time()
	print("numpy time:",end-start)


arr = np.ones((2,3),dtype=float)
print(arr)
arr1 = np.zeros(6,dtype=int)
print(arr1)
arr3 = np.array([[13,32,31],[64,25,76]],float)
arr4 = np.zeros_like(arr3)
print(arr4)
arr5 = np.ones_like(arr3)
print(arr5)
arr6 = np.array([1,3,2])
arr7 = np.array([3,4,6])
arr8 = np.vstack([[1,3,2],[3,4,6]])
print(arr8)
arr9 = np.random.rand(2,3)
print(arr9)
arr10 = np.array([2,5,6,5,5])
print(arr10[:3])
print(np.unique(arr10))
print(np.sort(arr10))
print(np.argsort(arr10))
np.random.shuffle(arr10)
isEqual = np.array_equal(arr9,arr10)
print(isEqual)
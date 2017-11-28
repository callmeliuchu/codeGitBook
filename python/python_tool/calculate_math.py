import numpy as np


class Calculator:
	def __init__(self):
		self.arr = []

	def push(self,arr):
		self.arr.append(arr)

	def t_sum(self):
		return np.sum(np.sum(np.array(vec)) for vec in self.arr)

	def tt_sum(self):
		return np.sum(np.sum(np.array(vec)**2) for vec in self.arr)

	def St(self):
		return  self.tt_sum() - self.t_sum()**2/sum(len(vec) for vec in self.arr)

	def Sa(self):
		return np.sum([np.sum(np.array(vec))**2/len(vec)  for vec in self.arr]) - self.t_sum()**2/sum(len(vec) for vec in self.arr)

	def Se(self):
		return self.St() - self.Sa()

	def na(self):
		return len(self.arr) - 1

	def ne(self):
		return np.sum(len(vec) for vec in self.arr) - len(self.arr)

	def Sa_(self):
		return self.Sa()/self.na()

	def Se_(self):
		return self.Se()/self.ne()

	def F(self):
		return self.Sa_()/self.Se_()

	def t(self):
		return 2.0595

	def u(self,index):
		return np.sum(self.arr[index])/len(self.arr[index])

	def range(self,index1,index2):
		u1 = self.u(index1)
		u2 = self.u(index2)
		gap = self.t()*((self.Se_()*(1/len(self.arr[index1])+1/len(self.arr[index2])))**0.5)
		us = u1 - u2 - gap
		ue = u1 - u2 + gap
		return [us,ue]



# A = [40,42,48,45,38]
# B = [26,28,34,32,30]
# C = [39,50,40,50,43]


A = [14,13,9,15,11,13,14,11]
B = [10,12,7,11,8,12,9,10,13,9,10,9]
C = [11,5,9,10,6,8,8,7]
cal = Calculator()
cal.push(A)
cal.push(B)
cal.push(C)
print(cal.range(0,1))
print(cal.range(0,2))
print(cal.range(1,2))
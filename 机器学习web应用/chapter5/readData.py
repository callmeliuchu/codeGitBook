import numpy as np
import pandas as pd
import copy
import collections
from scipy import linalg
import math
from collections import defaultdict



def imputation(inp,Ri):
	Ri = Ri.astype(float)
	def userav():
		for i in range(len(Ri)):
			Ri[i][Ri[i]==0] = sum(Ri[i])/float(len(Ri[i][R[i]]))
		return Ri
	def itemav():
		for i in range(len(Ri[0])):
			Ri[:,i][Ri[:,i]==0]=sum(Ri[:,i])/float(len(Ri[:,i][Ri[:,i]>0]))
		return Ri
	switch = {'useraverage':userav(),'itemaverage':itemav()}
	return switch[inp]






# df = pd.read_csv('utilitymatrix.csv')
# print(df)
# print(df.head(2))
# counts=collections.Counter([1,4,3,5])
# print(counts)
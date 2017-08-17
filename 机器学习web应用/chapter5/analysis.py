import numpy as np
import pandas as pd
import copy
import collections
from scipy import linalg
import math
from collections import defaultdict


def cross_validation(df,k):
	val_num = int(len(df)/float(k))
	print(val_num)
	df_trains = []
	df_vals = []
	for i in range(k):
		start_val = (k-i-1)*val_num
		end_val = start_val + val_num
		df_trains.append(pd.concat([df[:start_val],df[end_val:]]))
		df_vals.append(df[start_val:end_val])
	return df_trains,df_vals





df = pd.read_csv('utilitymatrix.csv')
print(df.head(4))
df_movies = pd.read_csv('movies_content.csv')
print(df_movies)
movies = df_movies.values[:,1:]
print('check:::',len(df.columns[1:]),'--',len(df_movies))
movielist = list(df.columns[1:])
nfolds = 5
df_trains,df_vals=cross_validation(df,nfolds)
print(len(df_trains))
print(len(df_vals))


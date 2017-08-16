import numpy as np
import pandas as pd
import copy
import collections
from scipy import linalg
import math
from collections import defaultdict
from scipy.stats import pearsonr
from scipy.spatial.distance import cosine



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


def sim(x,y,metric='cos'):
	if metric == 'cos':
		return 1.-cosine(x,y)
	else:
		return pearsonr(x,y)[0]


def CF_userbased(u_vec,K,data,indxs=False):
	def FindKNeighbours(r,data,K):
		neighs = []
		cnt = 0
		for u in range(len(data)):
			return 0




dfout=pd.read_csv("utilitymatrix.csv")
print(dfout)
df = pd.read_csv("ml-100k/u.data",sep="\t",header=None)
df_info = pd.read_csv("ml-100k/u.item",sep='|',header=None,encoding='iso8859-1')
moviescats = ['unknown','Action','Adventure','Animation','Children\'s','Comedy','Crime','Documentary',
              'Drama','Fantasy','Film-Noir','Horror','Musical','Mystery',
              'Romance','Sci-Fi','Thriller','War','Western']
movielist = [int(m.split(';')[1]) for m in dfout.columns[1:]]
dfout_movies = pd.DataFrame(columns=['movie_id']+moviescats)
startcatsindx = 5
cnt = 0
for m in movielist:
	dfout_movies.loc[cnt] = [m]+df_info.iloc[m-1][startcatsindx:].tolist()
	cnt = cnt + 1
print(dfout_movies.head)
dfout_movies.to_csv('movies_content.csv',index=None)

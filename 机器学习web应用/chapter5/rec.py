import numpy as np
import pandas as pd
import copy
import collections
from scipy import linalg
import math
from collections import defaultdict


df = pd.read_csv('ml-100k/u.data',sep='\t',header=None)
#movie list
df_info = pd.read_csv('ml-100k/u.item',sep='|',header=None,encoding='iso8859-1')
movielist = [df_info[1].tolist()[indx]+';'+str(indx+1) for indx in range(len(df_info[1].tolist()))]
nmovies = len(movielist)
nusers = len(df[0].drop_duplicates().tolist())  

min_ratings = 50
movies_rated  = list(df[1]) 
counts = collections.Counter(movies_rated)
print(counts)
dfout = pd.DataFrame(columns=['user']+movielist)

toremovelist = []
for i in range(1,nusers):
    tmpmovielist = [0 for j in range(nmovies)]
    dftmp =df[df[0]==i]
    for k in dftmp.index:
        if counts[dftmp.ix[k][1]]>= min_ratings:           
           tmpmovielist[dftmp.ix[k][1]-1] = dftmp.ix[k][2]
           
        else:
           toremovelist.append(dftmp.ix[k][1])
            
    dfout.loc[i] = [i]+tmpmovielist
  
toremovelist = list(set(toremovelist))
dfout.drop(dfout.columns[toremovelist], axis=1, inplace=True)
dfout.to_csv('utilitymatrix_1.csv',index=None)


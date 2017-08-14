import numpy as np
import pandas as pd
import copy
import collections
from scipy import linalg
import math
from collections import defaultdict


df = pd.read_csv("ml-100k/u.data",sep="\t",header=None)
df_info = pd.read_csv("ml-100k/u.item",sep='|',header=None,encoding='iso8859-1')
print(df)
# print(df_info)
# movielist = [df_info[1].tolist()[index]+";"+str(index+1) for index in range(len(df_info[1].tolist()))]
# print(movielist)
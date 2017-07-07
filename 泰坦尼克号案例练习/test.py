import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f():
	return 1

def data():
	#plt.rcParams['axes.unicode_minus']=False
	#plt.rcParams['font.sans-serif']=['SimHei']
	#plt.style.use('ggplot')
	path = 'F:\GitCodeBook\泰坦尼克号案例练习\Titanic'
	data=pd.read_csv(path+'/train.csv')
	return data.head(10)
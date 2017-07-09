import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif']=['SimHei']
plt.style.use('ggplot')


def loadDataByCSV(path):
	data = pd.read_csv(path)
	return data

def  trainData():
	path = 'F:\GitCodeBook\DataCompetiton/train.csv'
	return loadDataByCSV(path)

def  drawData(data):
	#用户动作类型数量统计
	fig = plt.figure(figsize=(10,10))
	fig.set(alpha=0.5)
	plt.subplot2grid((2,2),(0,0))
	data.action_type.value_counts().plot(kind='bar')
	plt.ylabel('action type number')
	plt.xlabel('action type')
	plt.show()
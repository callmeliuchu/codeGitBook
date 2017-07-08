import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif']=['SimHei']
plt.style.use('ggplot')

def data():
	path = 'F:\GitCodeBook\泰坦尼克号案例练习\Titanic'
	data=pd.read_csv(path+'/train.csv')
	data.head(10)
	return data

def showData(data):
	#统计存活和遇难
	fig = plt.figure(figsize=(10,10))
	fig.set(alpha=0.5)
	plt.subplot2grid((2,3),(0,0))
	data.Survived.value_counts().plot(kind='bar')
	plt.ylabel('people num')
	plt.title('passenger')
	#统计乘客等级分布
	plt.subplot2grid((2,3),(0,1))
	data.Pclass.value_counts().plot(kind='bar')
	plt.ylabel('people num')
	plt.title('passenger distribution')
	#统计获取者与遇难者的年龄分布
	plt.subplot2grid((2,3),(0,2))
	plt.scatter(data.Survived,data.Age)
	plt.ylabel('age')
	plt.grid(b=True,which='major',axis='y')
	plt.title('by age')
	#各个等级乘客年龄分布
	plt.subplot2grid((2,3),(1,0),colspan=2)
	data.Age[data.Pclass==1].plot(kind='kde')
	data.Age[data.Pclass==2].plot(kind='kde')
	data.Age[data.Pclass==3].plot(kind='kde')
	plt.xlabel('age')
	plt.ylabel('dense')
	plt.title('distribution')
	plt.legend(('1 level','2 level','3 level'),loc='best')
	#harbar distribution
	plt.subplot2grid((2,3),(1,2))
	data.Embarked.value_counts().plot(kind='bar')
	plt.title('number of people that climb the board')
	plt.ylabel('people num')
	plt.show()

def  SurviveInClass(data):
	fig = plt.figure(figsize=(5,5))
	fig.set(alpha=0.2)
	Survived_0 = data.Embarked[data.Survived==0].value_counts()
	Survived_1 = data.Embarked[data.Survived==1].value_counts()
	df = pd.DataFrame({u'live':Survived_1,u'not live':Survived_0})
	df.plot(kind='bar',stacked=True)
	plt.title(u'the situation of live')
	plt.xlabel(u'land')
	plt.ylabel(u'people number')
	plt.show()




strs = ['','','b']
newstr = [''.join(sorted(astr)) for astr in strs]
print(newstr)
index = 0
dictA = {}
for astr in newstr:
	if astr in dictA:
		dictA[astr].append(strs[index])
	else:
		dictA[astr]=[strs[index]]
	index = index + 1
res = []
for key in dictA:
	print(dictA[key])
	if len(dictA[key])>1:
		res.extend(dictA[key])
print(res)


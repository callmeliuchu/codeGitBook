import pandas as pd



df = pd.read_csv("train.csv",header=0)
#展示训练数据的每一项
# Data Dictionary
# Variable	Definition	Key
# survival 	Survival 	0 = No, 1 = Yes
# pclass 	Ticket class 	1 = 1st, 2 = 2nd, 3 = 3rd
# sex 	Sex 	
# Age 	Age in years 	
# sibsp 	# of siblings / spouses aboard the Titanic 	
# parch 	# of parents / children aboard the Titanic 	
# ticket 	Ticket number 	
# fare 	Passenger fare 	
# cabin 	Cabin number 	
# embarked 	Port of Embarkation
columns = df.columns
print(columns)
for column in columns:
	print(column)
	print(df[column].tolist())
	print("-------------------------------------------------------------------------------------------------")

#画图
# import os
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif']=['SimHei']
plt.style.use('ggplot')

# def data():
# 	path = 'F:\GitCodeBook\泰坦尼克号案例练习\Titanic'
# 	data=pd.read_csv(path+'/train.csv')
# 	data.head(10)
# 	return data

fig = plt.figure(figsize=(10,10))
fig.set(alpha=0.5)
#passenger survived
plt.subplot2grid((2,3),(0,0))

df.Survived.value_counts().plot(kind='bar')
plt.ylabel('people number')
plt.xlabel('survied or not')
plt.title('passenger survived')
#class level
plt.subplot2grid((2,3),(0,1))
df.Pclass.value_counts().plot(kind='bar')
plt.ylabel('class level number')
plt.xlabel('class level:0,1,2')
plt.title('class level distribution')
#统计获取者与遇难者的年龄分布
plt.subplot2grid((2,3),(0,2))
plt.scatter(df.Survived,df.Age)
plt.ylabel('age')
plt.grid(b=True,which='major',axis='y')
plt.title('distribution')
plt.show()


# def showData(data):
# 	#统计存活和遇难
# 	fig = plt.figure(figsize=(10,10))
# 	fig.set(alpha=0.5)
# 	plt.subplot2grid((2,3),(0,0))
# 	data.Survived.value_counts().plot(kind='bar')
# 	plt.ylabel('people num')
# 	plt.title('passenger')
# 	#统计乘客等级分布
# 	plt.subplot2grid((2,3),(0,1))
# 	data.Pclass.value_counts().plot(kind='bar')
# 	plt.ylabel('people num')
# 	plt.title('passenger distribution')
# 	#统计获取者与遇难者的年龄分布
# 	plt.subplot2grid((2,3),(0,2))
# 	plt.scatter(data.Survived,data.Age)
# 	plt.ylabel('age')
# 	plt.grid(b=True,which='major',axis='y')
# 	plt.title('by age')
# 	#各个等级乘客年龄分布
# 	plt.subplot2grid((2,3),(1,0),colspan=2)
# 	data.Age[data.Pclass==1].plot(kind='kde')
# 	data.Age[data.Pclass==2].plot(kind='kde')
# 	data.Age[data.Pclass==3].plot(kind='kde')
# 	plt.xlabel('age')
# 	plt.ylabel('dense')
# 	plt.title('distribution')
# 	plt.legend(('1 level','2 level','3 level'),loc='best')
# 	#harbar distribution
# 	plt.subplot2grid((2,3),(1,2))
# 	data.Embarked.value_counts().plot(kind='bar')
# 	plt.title('number of people that climb the board')
# 	plt.ylabel('people num')
# 	plt.show()

# def  SurviveInClass(data):
# 	fig = plt.figure(figsize=(5,5))
# 	fig.set(alpha=0.2)
# 	Survived_0 = data.Embarked[data.Survived==0].value_counts()
# 	Survived_1 = data.Embarked[data.Survived==1].value_counts()
# 	df = pd.DataFrame({u'live':Survived_1,u'not live':Survived_0})
# 	df.plot(kind='bar',stacked=True)
# 	plt.title(u'the situation of live')
# 	plt.xlabel(u'land')
# 	plt.ylabel(u'people number')
# 	plt.show()



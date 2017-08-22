import pandas as pd
import numpy as np
import random as rnd

import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier



train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
# train_columns = train_data.columns
# print(train_columns)
# train_data.Survived.value_counts().plot(kind='bar')
combine  = [train_data,test_data]
#columns
# ['PassengerId' 'Survived' 'Pclass' 'Name' 'Sex' 'Age' 'SibSp' 'Parch'
#  'Ticket' 'Fare' 'Cabin' 'Embarked']
print(train_data.columns.values)
# # print(train_data.head)
# print(train_data.info())
# print(train_data.describe())
#乘客类型
#    Pclass  Survived
# 0       1  0.629630
# 1       2  0.472826
# 2       3  0.242363
# print(train_data[['Pclass','Survived']])
Survived_result = train_data[['Pclass','Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
# print(Survived_result)
#性别生存率
#       Sex  Survived
# 0  female  0.742038
# 1    male  0.188908
Sex_result = train_data[['Sex','Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived',ascending=False)
# print(Sex_result)
#兄弟姐妹
# 1      1  0.535885
# 2      2  0.464286
# 0      0  0.345395
# 3      3  0.250000
# 4      4  0.166667
# 5      5  0.000000
# 6      8  0.000000
Sib_result = train_data[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='Survived',ascending=False)
# print(Sib_result)
#家庭
#    Parch  Survived
# 3      3  0.600000
# 1      1  0.550847
# 2      2  0.500000
# 0      0  0.343658
# 5      5  0.200000
# 4      4  0.000000
# 6      6  0.000000
Parch_result = train_data[['Parch','Survived']].groupby(['Parch'],as_index=False).mean().sort_values(by='Survived',ascending=False)
# print(Parch_result)
#    FamilySize  Survived
# 0           1  0.303538
# 1           2  0.552795
# 2           3  0.578431
# 3           4  0.724138
# 4           5  0.200000
# 5           6  0.136364
# 6           7  0.333333
# 7           8  0.000000
# 8          11  0.000000
for dataset in combine:
	dataset['FamilySize'] = dataset['SibSp']+dataset['Parch']+1
famility_result =  train_data[['FamilySize','Survived']].groupby(['FamilySize'],as_index=False).mean()
# print(famility_result)
#    IsAlone  Survived
# 0        0  0.505650
# 1        1  0.303538
for dataset in combine:
	dataset['IsAlone'] = 0
	dataset.loc[dataset['FamilySize']==1,'IsAlone']=1
IsAlone_result =  train_data[['IsAlone','Survived']].groupby(['IsAlone'],as_index=False).mean()
# print(IsAlone_result)
#年龄存活比例图
# g = sns.FacetGrid(train_data,col='Survived')
# g.map(plt.hist,'Age',bins=20)
# plt.show()
# grid = sns.FacetGrid(train_data,row='Embarked',col='Survived',size=2.2,aspect=1.6)
# grid.map(sns.barplot, 'Sex', 'Fare', alpha=.8, ci=None)
# grid.add_legend()
# plt.show()
# 重构数据集 - 去除Ticket,Cabin特征
train = train_data.drop(['Ticket','Cabin'],axis=1)
test = test_data.drop(['Ticket','Cabin'],axis=1)
combine = [train,test]
for dataset in combine:
	dataset['Salutation'] = train.Name.str.extract(' ([A-Za-z]+)\.',expand=False)
# print(pd.crosstab(['Salutation'],train['Sex']))
#   Salutation  Survived
# 0     Master  0.575000
# 1       Miss  0.702703
# 2         Mr  0.156673
# 3        Mrs  0.793651
# 4       Rare  0.347826
for dataset in combine:
    dataset['Salutation'] = dataset['Salutation'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Salutation'] = dataset['Salutation'].replace('Mlle', 'Miss')
    dataset['Salutation'] = dataset['Salutation'].replace('Ms', 'Miss')
    dataset['Salutation'] = dataset['Salutation'].replace('Mme', 'Mrs')
Salutation_result = train[['Salutation', 'Survived']].groupby(['Salutation'], as_index=False).mean()
# print(Salutation_result)
Salutation_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
for dataset in combine:
	dataset['Salutation'] = dataset['Salutation'].map(Salutation_mapping)
	dataset['Salutation'] = dataset['Salutation'].fillna(0)
# print(train.head())


train = train.drop(['Name','PassengerId'],axis=1)
test = test.drop(['Name'],axis=1)
# print(test)
# print(train.head)
combine = [train,test]
for dataset in combine:
	dataset['Sex'] = dataset['Sex'].map({'female':1,'male':0}).astype(int)
# print(train.head)
grid = sns.FacetGrid(train, row='Pclass', col='Sex')
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend()
# plt.show()
# print(train)
guess_ages = np.zeros((2,3))
# print(guess_age)
for dataset in combine:
	for i in range(0,2):
		for j in range(0,3):
			guess = dataset[(dataset['Sex']==i) & (dataset['Pclass']==j+1)]['Age'].dropna()
			age_guess = guess.median()
			guess_ages[i,j] = int(age_guess/0.5+0.5)*0.5

	for i in range(0,2):
		for j in range(0,3):
			dataset.loc[(dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j + 1), 'Age'] = guess_ages[i, j]
	dataset['Age'] = dataset['Age'].astype(int)
# print(train)
# 将年龄划分为5个年龄段,计算各段的存活率
#        AgeBand  Survived
# 0  (-0.08, 16]  0.550000
# 1     (16, 32]  0.337374
# 2     (32, 48]  0.412037
# 3     (48, 64]  0.434783
# 4     (64, 80]  0.090909
train['AgeBand'] = pd.cut(train['Age'],5)
AgeBand_result = train[['AgeBand','Survived']].groupby(['AgeBand'],as_index=False).mean().sort_values(by='AgeBand',ascending=True)
# print(AgeBand_result)
# print(train)
for dataset in combine:
	dataset.loc[dataset['Age']<=16,'Age'] =0
	dataset.loc[(dataset['Age']>16) & (dataset['Age']<=32),'Age'] =1
	dataset.loc[(dataset['Age']>32) & (dataset['Age']<=48),'Age'] =2
	dataset.loc[dataset['Age']>64,'Age'] =4

train = train.drop(['AgeBand'],axis=1)
combine = [train,test]
# print(train.head())



freq_port = train.Embarked.dropna().mode()[0]
# print(freq_port)

for dataset in combine:
	dataset['Embarked'] = dataset['Embarked'].fillna(freq_port)
Embarked_result = train[['Embarked','Survived']].groupby(['Embarked'],as_index=False).mean().sort_values(by='Survived', ascending=False)
# print(Embarked_result)

for dataset in combine:
	dataset['Embarked'] = dataset['Embarked'].map({'S':0,'C':1,'Q':2}).astype(int)
# print(train.head())

test['Fare'].fillna(test['Fare'].dropna().median(),inplace=True)

# 将票价切分为3段
train['FareBand'] = pd.qcut(train['Fare'],3)
# print(train)


FareBand_result = train[['FareBand','Survived']].groupby(['FareBand'],as_index=False).mean().sort_values(by='FareBand',ascending=True)
# print(FareBand_result)

for dataset in combine:
	dataset['Age*Class'] = dataset.Age*dataset.Pclass

# print(train.loc[:,['Age*Class','Age','Pclass']].head(10))
# 重构数据
for dataset in combine:
    dataset.loc[dataset['Fare'] <= 7.91, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare'] = 2
    dataset.loc[dataset['Fare'] > 31, 'Fare'] = 3
    dataset['Fare'] = dataset['Fare'].astype(int)

train = train.drop(['FareBand'],axis=1)
combine = [train,test]
print(train.head(10))

colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Feature correlations',y=1.05,size=15)
sns.heatmap(train.corr(),linewidth=0.1,vmax=1.0,square=True,cmap=colormap,linecolor='white',annot=True)
# plt.show()



#各种算法
# 1 逻辑回归 Logistic Regression
x_train = train.drop('Survived',axis=1)
y_train = train['Survived']
# print(x_train)
# print(y_train)
x_test = test.drop("PassengerId",axis=1).copy()
# print(x_test.head())
# print(x_train.shape,y_train.shape,x_test.shape)
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
y_pred = logreg.predict(x_test)
acc_log = round(logreg.score(x_train,y_train)*100,2)
# print(acc_log)
# print(y_pred)
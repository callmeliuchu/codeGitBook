import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot  as plt
import sklearn
from scipy import stats
filePath = "F:\codeGitBook\kaggle\HousePrices/"




df = pd.read_csv(filePath+"train.csv")
df1 = pd.read_csv(filePath+"test.csv")
df_train = pd.read_csv(filePath+"train.csv")
dfnum = df.select_dtypes(include = ['float64','int64'])


def showSalePrice():
	print(df[['SalePrice']])
	sns.distplot(df[['SalePrice']],kde=False,color='g',bins=200)
	plt.show()


def showCorrelate():
	print(dfnum.corr()['SalePrice'])
	dfnum_corr = dfnum.corr()['SalePrice'][:-1]
	golden_feature_list = dfnum_corr[abs(dfnum_corr) > 0.5].sort_values(ascending = False)
	print(golden_feature_list)

def showAllNumberVar():
	cm1 = dfnum.hist(figsize=(16,20),bins=50,xlabelsize=8,ylabelsize=8)
	plt.show()


def  showHeatMap():
	dfnum_corr1 = dfnum.corr()
	cols = dfnum_corr1.nlargest(10,'SalePrice')['SalePrice'].index
	cm = np.corrcoef(dfnum[cols].values.T)
	hm = sns.heatmap(cm,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size':10},yticklabels=cols.values, xticklabels=cols.values)
	plt.show()


def showColums(var):
	# print(df_train.columns)
	# print(df_train['SalePrice'].describe())
	# sns.distplot(df_train['SalePrice'],kde=False)
	# print("skewness:%f" % df_train['SalePrice'].skew())
	var = 'GrLivArea'
	data = pd.concat([df_train['SalePrice'],df_train[var]],axis=1)
	data.plot.scatter(x=var,y='SalePrice',ylim=(0,800000))
	plt.show()


def showRelation(var):
	data = pd.concat([df_train['SalePrice'],df_train[var]],axis=1)
	data.plot.scatter(x=var,y='SalePrice',ylim=(0,800000))
	plt.show()

def showColumsRelation():
	columns = dfnum.columns
	for column in columns:
		showRelation(column)


showColumsRelation()

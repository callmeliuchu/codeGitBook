import sklearn
path = "F:/anaconda/Anaconda/Lib/site-packages/sklearn/datasets/data/boston_house_prices.csv"
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error
df = pd.read_csv(path,header=None)
x=df[df.columns[:-1]][2:].values
y=df[df.columns[-1]][2:].values


def printMean(scores):
	print("mean %0.2f (+/- %0.2f)"%(scores.mean(),scores.std()*2))





print("line regression")
cv=10
model=LinearRegression()
scores = cross_validation.cross_val_score(model,x,y,cv=cv)
printMean(scores)
predicted = cross_validation.cross_val_predict(model,x,y,cv=cv)
print("mse:",mean_squared_error(y,predicted))



print("ridge regression")
cv=10
model=Ridge(alpha=1.0)
scores = cross_validation.cross_val_score(model,x,y,cv=cv)
printMean(scores)
predicted = cross_validation.cross_val_predict(model,x,y,cv=cv)
print("mse:",mean_squared_error(y,predicted))


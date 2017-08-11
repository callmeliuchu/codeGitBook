import sklearn
path = "F:/anaconda/Anaconda/Lib/site-packages/sklearn/datasets/data/boston_house_prices.csv"
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error
df = pd.read_csv(path,header=None)
x=df[df.columns[:-1]][2:].values
y=df[df.columns[-1]][2:].values
print(y)
y=list(map(float,y))
print(df)
print(x)
print(y)
cv=10
print("line regression")
lin=LinearRegression()
scores = cross_validation.cross_val_score(lin,x,y,cv=cv)
print(scores.std()*2)
predicted = cross_validation.cross_val_predict(lin,x,y,cv=cv)
print(mean_squared_error(y,predicted))
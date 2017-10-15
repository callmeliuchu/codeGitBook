#获取数据
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np



#加载数据
data = load_iris()
print(data)
#获取每一个属性
features = data['data']
feature_names = data['target_names']
target = data['target']
print(features,feature_names,target)
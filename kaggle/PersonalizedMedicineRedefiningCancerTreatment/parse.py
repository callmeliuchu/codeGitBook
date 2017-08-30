import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict


# def readFile(path):
# 	with open(path,encoding='utf8') as f:
# 		return f.read()


# training_variants_data = pd.read_csv('training_variants',sep=",")
# test_variants_data = pd.read_csv('test_variants',sep=',')
# train_text = readFile("F:/代码日记/training_text")
# test_text = readFile("F:/代码日记/test_text")




# print(training_variants_data)
# print(test_variants_data)
# print(train_text)
# print(test_text)




df_train_txt = pd.read_csv('F:/代码日记/training_text',sep='\|\|',header=None,skiprows=1,names=['ID','Text'],engine='python')
# print(df_train_txt.head())
df_train_var = pd.read_csv('training_variants')
# print(df_train_var.head())
df_test_txt = pd.read_csv('F:/代码日记/test_text',sep='\|\|',header=None,skiprows=1,names=['ID','Text'],engine='python')
# print(df_test_txt.head())
df_test_var = pd.read_csv('test_variants')
# print(df_test_var.head())

df_train = pd.merge(df_train_var,df_train_txt,how='left',on='ID')
print(df_train.head())

df_test = pd.merge(df_test_var,df_test_txt,how='left',on='ID')
print(df_test.head())


print(df_train.describe(include='all'))
print(df_test.describe(include='all'))


# df_train['Class'].value_counts().plot(kind='bar',rot=0)
# plt.show()
print(df_train.shape)
df_train,val = train_test_split(df_train,test_size=0.7,random_state=8,stratify=df_train['Class'])
# print(df_train.head())
print(df_train.shape)
print(val.shape)



def evaluate_features(X,y,clf=None):
	if clf is None:
		clf = LogisticRegression()
	probas = cross_val_predict(clf,X,y,cv=StratifiedKFold(random_state=8),n_jobs=-1,method='predict_proba',verbose=2)
	pred_indices = np.argmax(probas,axis=1)
	classes = np.unique(y)
	preds = classes[pred_indices]
	skplt.plot_confusion_matrix(y,preds)
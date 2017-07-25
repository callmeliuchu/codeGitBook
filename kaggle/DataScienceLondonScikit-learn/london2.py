import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score



x_train =  pd.read_csv('F:\codeGitBook\kaggle\DataScienceLondonScikit-learn/train.csv');
y_train = pd.read_csv('F:\codeGitBook\kaggle\DataScienceLondonScikit-learn/trainLabels.csv')
x_test = pd.read_csv('F:\codeGitBook\kaggle\DataScienceLondonScikit-learn/test.csv')
x_train = np.asarray(x_train)
y_train = np.asarray(y_train)
x_test = np.asarray(x_test)
y_train = y_train.ravel()
# print(x_train)
# print(y_train)
# print(x_test)


x_all = np.r_[x_train,x_test]
# print(x_all)
# print(x_all.shape)


from sklearn.mixture import GaussianMixture
lowest_bic = np.infty
bic = []
n_components_range = range(1,7)
cv_types = ['spherical','tied','diag','full']
for cv_type in cv_types:
	for n_components in n_components_range:
		gmm = GaussianMixture(n_components=n_components_range,covariance_type=cv_type)
		gmm.fit(x_all)
		bic.append(gmm.aic(x_all))
		if bic[-1] < lowest_bic:
			lowest_bic = bic[-1]
			best_gmm = gmm

best_gmm.fit(x_all)
x_train = best_gmm.predict_proba(x_train)
x_test = best_gmm.predict_proba(x_test)
print(x_train)
print(x_test)


import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score



x_train =  pd.read_csv('F:\codeGitBook\kaggle\DataScienceLondonScikit-learn/train.csv');
y_train = pd.read_csv('F:\codeGitBook\kaggle\DataScienceLondonScikit-learn/trainLabels.csv')
x_test = pd.read_csv('F:\codeGitBook\kaggle\DataScienceLondonScikit-learn/test.csv')
# print(x_test)
# print(x_train)
# print(y_train)
x_train = np.asarray(x_train)
y_train = np.asarray(y_train)
x_test = np.asarray(x_test)
y_train = y_train.ravel()
print("x_train list---------------------------------------------------")
print(len(x_train))
print(x_train)
print("x_train list---------------------------------------------------")
print("y_train list---------------------------------------------------")
print(len(y_train))
print(y_train)
print("y_train list---------------------------------------------------")
print("x_test list---------------------------------------------------")
print(len(x_test))
print(x_test)
print("x_test list---------------------------------------------------")


x_all = np.r_[x_train,x_test]
print("x_all-----------------------------------------------------------")
print(len(x_all))
print(x_all)
print(x_all.shape)
print("x_all-----------------------------------------------------------")


from sklearn.mixture import GaussianMixture
lowest_bic = np.infty
bic = []
n_components_range = range(1,7)
cv_types = ['spherical','tied','diag','full']
for cv_type in cv_types:
	for n_components in n_components_range:
		gmm = GaussianMixture(n_components=n_components,covariance_type=cv_type)
		gmm.fit(x_all)
		bic.append(gmm.aic(x_all))
		if bic[-1] < lowest_bic:
			lowest_bic = bic[-1]
			best_gmm = gmm

print("best..........................................................................")
print(best_gmm)
best_gmm.fit(x_all)
x_train = best_gmm.predict_proba(x_train)
x_test = best_gmm.predict_proba(x_test)
print(x_train)
print(x_test)
print("best..........................................................................")

knn = KNeighborsClassifier()
rf = RandomForestClassifier()

param_grid = dict()
grid_search_knn = GridSearchCV(knn,param_grid=param_grid,cv=10,scoring='accuracy').fit(x_train,y_train)
# print(grid_search_knn.best_estimator_)
# print(grid_search_knn.best_estimator_.score(x_train,y_train))
knn_best = grid_search_knn.best_estimator_
grid_search_rf = GridSearchCV(rf,param_grid=dict(),verbose=3,scoring='accuracy',cv=10).fit(x_train,y_train)
# print(grid_search_rf.best_estimator_)
# print(grid_search_rf.best_estimator_.score(x_train,y_train))
rf_best = grid_search_rf.best_estimator_

knn_best.fit(x_train,y_train)
# print(knn_best.predict(x_test)[0:10])
rf_best.fit(x_train,y_train)
# print(rf_best.predict(x_test)[0:10])

knn_score = cross_val_score(knn_best,x_train,y_train,cv=10,scoring='accuracy').mean()
# print(knn_score)
rf_score = cross_val_score(rf_best,x_train,y_train,cv=10,scoring='accuracy').mean()
# print(rf_score)


knn_best_pred = pd.DataFrame(knn_best.predict(x_test))
rf_best_pred = pd.DataFrame(rf_best.predict(x_test))
knn_best_pred.index+=1
rf_best_pred.index+=1
print("----------------")
print(knn_best_pred)
print("----------------")
# print(knn_best_pred)
# print(rf_best_pred)
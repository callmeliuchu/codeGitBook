import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt



x = np.arange(1,101,1).astype(float)
print(x)
y = 2*np.arange(1,101,1).astype(float)
print(y)
noise = np.random.normal(0,10,100)
print(noise)
y = y + noise
print(y)
fig = plt.figure(figsize=(10,10))
plt.plot(x,y,'ro')
plt.axis([0,102,-20,220])
plt.quiver(60,100,10-0,20-0,scale_units='xy',scale=1)
plt.arrow(60,100,10-0,20-0,head_width=2.5,head_length=2.5,fc='k',ec='k')
plt.text(70,110,r'$v^1$',fontsize=20)
ax=fig.add_subplot(111)
ax.axis([0,102,-20,220])
ax.set_xlabel('x',fontsize=40)
ax.set_ylabel('y',fontsize=40)
fig.suptitle('2 dimensional datset',fontsize=40)
fig.savefig('pca_data.png')
# plt.show()
mean_x=np.mean(x)
mean_y=np.mean(y)
u_x=(x-mean_x)/np.std(x)
u_y=(y-mean_y)/np.std(y)
sigma=np.cov([u_x,u_y])
eig_vals,eig_vecs=np.linalg.eig(sigma)
print(eig_vecs)
eig_pairs=[(np.abs(eig_vals[i]),eig_vecs[:,i]) for i in range(len(eig_vecs))]
print(eig_pairs)
eig_pairs.sort()
eig_pairs.reverse()
v1=eig_pairs[0][1]
print(v1)
x_v1=v1[0]*np.std(x)+mean_x
y_v1=v1[1]*np.std(y)+mean_y
print((y_v1-1)/(x_v1-1))
x=np.array([u_x,u_y])
x=x.T
pca=PCA(n_components=1)
pca.fit(x)
v1_sklearn=pca.components_[0]
print(v1_sklearn)
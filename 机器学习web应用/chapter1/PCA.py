import numpy as np
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
plt.show()
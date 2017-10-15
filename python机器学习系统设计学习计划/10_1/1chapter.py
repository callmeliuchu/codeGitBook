import numpy as np
a = np.array([0,1,2,3,4,5])
print(a.shape)
b = a.reshape((3,2))
c = a.reshape((3,2)).copy()
c[1][0] = 555
print(c)
print(a)
print(a*2)
print(a**2)
print([1,2,3,4,5]*2)
print(a[[1,2,5]])
print(a>4)
print(a[a>4])
# print(a.clip(0,4))
print(b)
print(b.clip(0,4))
c = np.array([1,2,np.NAN,3,4])
print(c)
print(np.isnan(c))
print(np.mean(c[~np.isnan(c)]))
# import timeit
# normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))',
# 	number=10000)
# navie_np_sec = timeit.timeit('sum(na*na)',
# 	setup="import numpy as np;na = np.arange(1000)",
# 	number=10000)
# good_np_sec = timeit.timeit('na.dot(na)',
# 	setup="import numpy as np;na=np.arange(1000)",
# 	number=10000)
# print(normal_py_sec)
# print(navie_np_sec)
# print(good_np_sec)
a = np.array([1,2,3])
print(a.dtype)
b = np.array([1,"stringy"])
print(b)
c = np.array([1,"string",set([1,23,5])])
print(c.dtype)
import scipy as sp
print(sp.version.full_version)
print(sp.dot is np.dot)


def error(f,x,y):
	return sp.sum((f(x)-y)**2)


def draw_x_y():
	data = sp.genfromtxt("web_traffic.tsv",delimiter="\t")
	print(data)
	print(data[:10])
	print(data.shape)
	x = data[:,0]
	y = data[:,1]
	# print(x,y)
	# print(sp.sum(sp.isnan(y)))
	x = x[~np.isnan(y)]
	y = y[~np.isnan(y)]
	import matplotlib.pyplot as plt
	fp1,residuals,rank,sv,rcond = sp.polyfit(x,y,100,full=True)
	f1 = sp.poly1d(fp1)
	fx = sp.linspace(0,x[-1],1000)
	plt.plot(fx,f1(fx),linewidth=4)
	plt.legend(["d=%i"%f1.order],loc="upper left")
	plt.scatter(x,y)
	plt.title('web traffic over the last month')
	plt.xlabel('Time')
	plt.ylabel('hits/hour')
	plt.xticks([w*7*24 for w in range(10)],
		['week %i'%w for w in range(10)])
	plt.autoscale(tight=True)
	plt.grid()
	plt.show()

draw_x_y()
# draw_x_y()
# data = sp.genfromtxt("web_traffic.tsv",delimiter="\t")
# print(data)
# print(data[:10])
# print(data.shape)
# x = data[:,0]
# y = data[:,1]
# # print(x,y)
# # print(sp.sum(sp.isnan(y)))
# x = x[~np.isnan(y)]
# y = y[~np.isnan(y)]
# fp1,residuals,rank,sv,rcond = sp.polyfit(x,y,1,full=True)
# print(fp1)
# f1 = sp.poly1d(fp1)
# # print(f1)
# print(error(f1,x,y))

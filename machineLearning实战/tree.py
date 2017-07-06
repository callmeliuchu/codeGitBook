from math import log

#计算香农熵，数据格式[1,2,1,2,3..,label]
def calcShannonEnt(dataSet):
	m = len(dataSet)
	count ={}
	#用字典收集数据
	for data in dataSet:
		label = data[-1]
		if label in count:
			count[lable]=count[label]+1
		else:
			count[label]=1
	#计算香农熵即p*log(2,p)求和
	shanno = 0.0
	for key in count:
		p = count[key]/float(m)
		shanno = shanno - p*log(2,p)
	return shanno

#利用书上造的例子
def createData():
	dataSet = [[1,1,'yes'],
	           [1,1,'yes'],
	           [1,0,'no'],
	           [0,1,'no'],
	           [0,1,'no']]
	labels = ['no surfacing','flippers']
	#每一列的特征值，除了最后一列表示分类标签
	return dataSet,labels

def splitDataSet(dataSet,axis,value):
	retMat = []
	for data in dataSet:
		if data[axis]==value:
			#去除对应轴
			vec = data[:axis]
			vec.extend(data[axis+1:])
			retMat.append(vec)
	return retMat



data = createData()
print(data)

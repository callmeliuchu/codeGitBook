from math import log
import operator 

#计算香农熵，数据格式[1,2,1,2,3..,label]
def calcShannonEnt(dataSet):
	m = len(dataSet)
	count ={}
	#用字典收集数据
	for data in dataSet:
		label = data[-1]
		if label in count:
			count[label]=count[label]+1
		else:
			count[label]=1
	#计算香农熵即p*log(2,p)求和
	shanno = 0.0
	for key in count:
		p = count[key]/float(m)
		shanno = shanno - p*log(p,2)
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


def chooseBestFeatureToSplit(dataSet):
	n = len(dataSet[0])-1
	m = len(dataSet)
	baseShanno = calcShannonEnt(dataSet)
	bestGain = 0.0
	bestFeature = -1
	for i in range(n):
		vecList = [arr[i] for arr in dataSet]
		nums = set(vecList)
		shannoSum  = 0.0
		for num in nums:
			data=splitDataSet(dataSet,i,num)
			shanon=calcShannonEnt(data)
			p = float(len(data))/len(dataSet)
			shannoSum = shannoSum + p*shanon
		gain = baseShanno - shannoSum
		if gain > bestGain:
			bestGain = gain
			bestFeature = i
	return bestFeature


def majorityCnt(classList):
	count = {}
	for val in  classList:
		if val not in count:
			count[val]=0
		count[val]=count[val]+1
	sortedList = sorted(count.items(),key=operator.itemgetter(1),reverse=True)
	return sortedList[0][0]


def createTree(dataSet,labels):
	classList = [data[-1] for data in dataSet]
	if classList.count(classList[0])==len(classList):
		return classList[0]
	if len(classList[0])==1:
		return majorityCnt(classList)
	bestFeature = chooseBestFeatureToSplit(dataSet)
	bestLabel = labels[bestFeature]
	tree = {bestLabel:{}}
	del labels[bestFeature]
	collectData = [data[bestFeature] for data in dataSet]
	numSet = set(collectData)
	for num in numSet:
		sublabels = labels[:]
		newDataSet = splitDataSet(dataSet,bestFeature,num)
		tree[bestLabel][num]=createTree(newDataSet,sublabels)
	return tree
	





data,labels= createData()
tree = createTree(data,labels)
print(tree)






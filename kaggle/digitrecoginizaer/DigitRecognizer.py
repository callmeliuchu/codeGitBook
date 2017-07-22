import csv
import time
import numpy as np
import operator

path = "F:\codeGitBook\kaggle\digitrecoginizaer/train.csv"
testPath =  "F:\codeGitBook\kaggle\digitrecoginizaer/test.csv"
submitPath = "F:\codeGitBook\kaggle\digitrecoginizaer/submit.csv"

def showData(path):
	with open(path,encoding='utf8') as f:  
		csv_reader = list(csv.reader(f))
		for row in csv_reader:
			#row = csv_reader[0]
			label = row[0]
			vec = row[1:]
			print("-----------------------------------------------------------------")
			time.sleep(1)
			for i in range(28):
				print("\t".join(vec[i*28:(i+1)*28]))


def finalVal(val):
	if val==0:
		return 0
	return 1

def loadDataSet(file):
	returnMat = []
	labels = []
	with open(file,encoding='utf8') as f:
		lines = list(csv.reader(f))
		for i in range(1,len(lines)):
			line = lines[i]
			labels.append(line[0])
			data = [finalVal(int(line[i]))  for i in range(1,len(line))]
			returnMat.append(data)
	return np.array(returnMat),labels


def loadTestDataSet(file):
	returnMat = []
	with open(file,encoding='utf8') as f:
		lines = list(csv.reader(f))
		for i in range(1,len(lines)):
			data = [finalVal(int(d))  for d in lines[i]]
			returnMat.append(data)
	return np.array(returnMat)


def knn(vec,trainDataSet,labels,k=3):
	tempDataSet = trainDataSet - vec
	tempDataSet = tempDataSet**2
	sumVec = tempDataSet.sum(axis=1)
	sumVec = sumVec**0.5
	sortedIndex = sumVec.argsort()
	count = {}
	for i in range(k):
		index = sortedIndex[i]
		label = labels[index]
		if label not in count:
			count[label] = 0
		count[label] = count[label] + 1
	sortedCount = sorted(count.items(),key=operator.itemgetter(1),reverse=True)
	return sortedCount[0][0]


def showNum(vec):
	for i in range(28):
		print(vec[i*28:(i+1)*28])





def writeRowToCSV(file,result):
	with open(file,'wb') as f:
		mywriter = csv.writer(f)
		for row in result:
			mywriter.write(row)




#showData(testPath)
# dataSet,label=loadDataSet(path)
# print(np.shape(dataSet))
# print(dataSet)
# showData(path)
def predict():
	result = []
	trainData,labels= loadDataSet(path)
	testData = loadTestDataSet(testPath)
	index = 1
	mywriter = csv.writer(open(submitPath,'w',newline=''))
	for vec in testData:
		predictNum = knn(vec,trainData,labels,5)
		#result.append([index,predict])
		# print(predictNum)
		# showNum(vec)
		mywriter.writerow([index,predictNum])
		index = index + 1



predict()
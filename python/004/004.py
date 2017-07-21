import re
from collections import Counter

def getDataList(fileName):
	f = open(fileName)
	lines = f.readlines()
	datalist = []
	for line in lines:
		data = line.strip()
		data = re.sub('\.|,|\"','',data)
		datalist.extend(data.split(' '))
	return datalist

def wc(fileName):
	print(Counter(getDataList(fileName)))


if __name__=="__main__":
	fileName = "F:\codeGitBook\python/004/test.txt"
	wc(fileName)



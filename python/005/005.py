import re
import os
from collections import Counter

def getDataList(fileName):
	datalist = []
	with open(fileName) as f:
		lines = f.readlines()
		for line in lines:
			data = line.strip()
			data = re.sub("\"|,|\.","",data)
			datalist.extend(data.split(" "))
	return datalist


def count(datalist):
	print(datalist)
	return Counter(datalist)



def countByFile(file):
	print(count(getDataList(fileName)))


file = "F:\codeGitBook\python/005"
filelist = os.listdir(file)
for fileName in filelist:
	path = file + "/" + fileName
	countByFile(path)

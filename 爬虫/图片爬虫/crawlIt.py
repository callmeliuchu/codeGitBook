import re
import urllib.request
import json
import os
import socket
filePath = 'F:/codeGitBook/爬虫/图片爬虫/mmpic/data.txt'
dataSet = {}
def craw(url,aid):
	try:
		html1 = urllib.request.urlopen(url).read()
		html1 = str(html1)
		paturl = "(http://dlpic.fungood.cn/uploads/.*?.jpg)"
		location = "F:/codeGitBook/爬虫/图片爬虫/mmpic/"
		result = re.compile(paturl).findall(html1)[0]
		dataSet[aid]=result
		print(result)
		#urllib.request.urlretrieve(result,filename=location+aid+".jpg")
	except urllib.error.URLError as e:
		print(url+"  "+str(e))


aurl = "http://www.douluo123.com/shaonvmanhua/114"

def runCrawl():
	if os.path.isfile(filePath):
		return	
	for j in range(200,220):
		file = "F:/codeGitBook/爬虫/图片爬虫/mmpic/"+str(j)
		if not os.path.isfile(file):
			os.mkdir("F:/codeGitBook/爬虫/图片爬虫/mmpic/"+str(j))
		url = aurl + str(j)
		turl = aurl + str(j) +".html"
		html1 = urllib.request.urlopen(turl).read()
		html1 = str(html1)
		pat = "<b>(.*?)</b>"
		result = re.compile(pat).findall(html1)[1]
		craw(turl,str(j)+"_"+str(1))
		for i in range(2,int(result)+1):
			trueurl = url + "_" + str(i) + ".html"
			craw(trueurl,str(j)+"_"+str(i))


def writeJson(dataSet):
	if os.path.isfile(filePath):
		return
	f = open(filePath,'w')
	f.write(json.dumps(dataSet))
	f.close()

def readJson(file):
	f = open(filePath,'r')
	data = json.loads(f.read())
	f.close()
	return data

def getDataSet():
	runCrawl()
def loadPic():
	socket.setdefaulttimeout(5.0)
	for key,value in data.items():
		num = key.split(".")[0].split("_")[0]
		location = "F:/codeGitBook/爬虫/图片爬虫/mmpic/"+num+"/"
		print(location)
		try:
			urllib.request.urlretrieve(value,filename=location+key+".jpg")
		except Exception as e:
			print(str(e))
		print(key,value)


getDataSet()
writeJson(dataSet)
data = readJson(filePath)
loadPic()

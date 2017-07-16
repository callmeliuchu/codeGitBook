import re
import urllib.request
import codecs
import json
import pymysql
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root")
conn1=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mydb2")

filePath = "F:\codeGitBook\爬虫\数据爬虫\花椒/"

def saveFile(filePath,data):
	with open(filePath,'wb') as f:
		f.write(data)

def readFile(filePath):
	with open(filePath,'rb') as f:
		return f.read().decode('utf-8')


def crawl(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	path = filePath + "index.html"
	saveFile(path,data)
	return data.decode('utf-8')

def readHTML(name):
	path = filePath + name
	return readFile(path)


def parseData():
	data = readHTML("copy.htm").replace('\n','').replace('\r','')
	patLink = "\"(http://www.huajiao.com/l/.*?)\""
	links = re.compile(patLink).findall(data)
	userArr = []
	ret = {}
	file = filePath + "huajiaoData.json"
	for url in links:
		try:
			vec = parseUser(url)
			if len(vec[0])>0:
				userArr.append(vec)
		except Exception as e:
			print(str(e))
	ret['data']=userArr
	writeJson(file,ret)


def writeArr(file,vec):
	f = codecs.open(file,'w','utf-8')
	f.write(str(vec)+'\r\n')





def parseUser(userUrl="http://www.huajiao.com/l/134153325"):
	data = crawl(userUrl).replace('\n','').replace('\r','')
	patUser = "<div class=\"content author-info-box\">(.*?)switch js-switch"
	userContent = re.compile(patUser).findall(data)
	print(userContent)
	patName = "js-ulink js-nickname link.*?<h3>(.*?)</h3>"
	name = re.compile(patName).findall(data)
	print(name)
	patWhatches = "number js-watches.*?>(.*?)<"
	whatches = re.compile(patWhatches).findall(data)
	print(whatches)
	patFans = "number js-fans.*?>(.*?)<"
	fans = re.compile(patFans).findall(data)
	print(fans)
	patHuajiao = "number js-currency.*?>(.*?)<"
	huajiao = re.compile(patHuajiao).findall(data)
	print(huajiao)
	return [name[0].strip(),whatches[0].strip(),fans[0].strip(),huajiao[0].strip()]


def writeJson(file,data):
	with open(file, 'w') as f:
		json.dump(data, f)	

def readJson(file):
	with open(file, 'r') as f:
		data = json.load(f)
		return data

def readData():
	file = filePath + "huajiaoData.json"
	data = readJson(file)
	return data

def readArr():
	file = filePath + "huajiao.json"
	f = open(file,'rb')
	dataObj = json.load(f)
	print(dataObj)


def createDB():
	val=conn.query("create database huajiao")
	print(val)

def insertIntoDB(data):
	sql = "INSERT into exam"+\
	"(user_name,user_whatch_num,user_fans_num"+\
	",user_pepper_money)values("+data+")"
	return sql

def exexute(insertSql):
	print(insertSql)
	cs = conn1.cursor()
	val=cs.execute(insertSql)
	conn1.commit()


def insertJsonToDB():
	data = readData()
	arr = data['data']
	re_h=re.compile('</?\w+[^>]*>')
	print(len(arr))
	userid = 0 
	for vec in arr:
		vec[0] = re_h.sub('',vec[0])
		print(vec)
		#vec[0] = "user" + str(userid)
		# userid = userid + 1
		# newVec = ["'"+e+"'" for e in vec]
		# value = ",".join(newVec)
		# sqlStr = insertIntoDB(value)
		# exexute(sqlStr)



insertJsonToDB()
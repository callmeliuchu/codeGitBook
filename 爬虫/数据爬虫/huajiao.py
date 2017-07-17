import re
from DBConnect import exexute
from FileDeal import *
from Spider import crawl

filePath = "F:\codeGitBook\爬虫\数据爬虫\花椒/"


def readHTML(name):
	path = filePath + name
	return readFile(path)


def parseData(data,fileName="data.json"):
	#data = readHTML("copy.htm").replace('\n','').replace('\r','')
	patLink = "\"(http://www.huajiao.com/l/.*?)\""
	links = re.compile(patLink).findall(data)
	userArr = []
	ret = {}
	file = filePath + fileName
	for url in links:
		try:
			vec = parseUser(url)
			if len(vec[0])>0:
				userArr.append(vec)
		except Exception as e:
			print(str(e))
	ret['data']=userArr
	writeJson(file,ret)


def parseUser(userUrl):
	data = crawl(userUrl).replace('\n','').replace('\r','')
	patUser = "<div class=\"content author-info-box\">(.*?)switch js-switch"
	userContent = re.compile(patUser).findall(data)
	patName = "js-ulink js-nickname link.*?<h3>(.*?)</h3>"
	name = re.compile(patName).findall(data)
	patWhatches = "number js-watches.*?>(.*?)<"
	whatches = re.compile(patWhatches).findall(data)
	patFans = "number js-fans.*?>(.*?)<"
	fans = re.compile(patFans).findall(data)
	patHuajiao = "number js-currency.*?>(.*?)<"
	huajiao = re.compile(patHuajiao).findall(data)
	return [name[0].strip(),whatches[0].strip(),fans[0].strip(),huajiao[0].strip()]


def readData(fileName):
	file = filePath + fileName
	data = readJson(file)
	return data

def insertIntoDB(data):
	sql = "INSERT into pepper_tbl"+\
	"(user_name,user_whatch_num,user_fans_num"+\
	",user_pepper_money)values("+data+")"
	return sql




def insertJsonToDB(fileName):
	data = readData(fileName)
	arr = data['data']
	re_h=re.compile('</?\w+[^>]*>')
	#print(len(arr))
	userid = 0 
	for vec in arr:
		vec[0] = re_h.sub('',vec[0])
		print(vec)
		#vec[0] = "user" + str(userid)
		#userid = userid + 1
		newVec = ["'"+e+"'" for e in vec]
		value = ",".join(newVec)
		sqlStr = insertIntoDB(value)
		exexute(sqlStr)


insertJsonToDB("huajiaoData_1.json")

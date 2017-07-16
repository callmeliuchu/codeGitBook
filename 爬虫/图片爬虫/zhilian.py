import re
import urllib.request
import os
import csv
filePath = "F:\codeGitBook\爬虫\图片爬虫\智联/"
def saveFile(filePath,data):
	with open(filePath,'wb') as f:
		f.write(data)

def readFile(filePath):
	with open(filePath,'rb') as f:
		return f.read().decode('utf-8')

def test():
	url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8D%97%E4%BA%AC&kw=python%E5%BC%80%E5%8F%91&sm=0&p=2"
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	if os.path.isfile(filePath):
		return
	saveFile(filePath,data)
	data = str(data)
	print(data)

def readHtml():
	if not os.path.isfile(filePath):
		return
	return readFile(filePath)


def parse(data):
	patContent = "(<table.*?>.*?</table>)"
	dataArr = re.compile(patContent).findall(data)
	infoArr = []
	retArr = []
	head=['jobName','jobLink','feedBack','comLink','comName','salary','place','releaseDate','detail']
	res = {}
	res['head']=head
	for i in range(1,len(dataArr)):
		d = dataArr[i]
		info,arr= parseDataConttent(d)
		infoArr.append(info)
		retArr.append(arr)
	res['content']=retArr
	return {'baseInfo':infoArr,'head':head},res


def  getContentByRe(pattern,data):
	return re.compile(pattern).findall(data)



def parseDataConttent(data):
	patJob = '<a.*?href="(http://jobs.zhaopin.com/.*?.htm).*?>(.*?)</a>'
	jobArr = re.compile(patJob).findall(data)
	patFkLv = "<td.*?class=\"fk_lv\"><span>(.*?)</span></td>"
	feedBack = re.compile(patFkLv).findall(data)
	patCom = "<td class=\"gsmc\"><a href=\"(http://.*?)\".*?>(.*?)</a></td>"
	comArr = re.compile(patCom).findall(data)
	patZwyx = "<td class=\"zwyx\">(.*?)</td>"
	jobSalary = re.compile(patZwyx).findall(data)
	patGzdd = "<td class=\"gzdd\">(.*?)</td>"
	jobPlace = re.compile(patGzdd).findall(data)
	patGxsj = "<td class=\"gxsj\"><span>(.*?)</span>"
	releaseDate = re.compile(patGxsj).findall(data)
	patDeatil = "<li class=\"newlist_deatil_two\"><span>(.*?)</li>"
	detail = re.compile(patDeatil).findall(data)[0]
	re_h=re.compile('</?\w+[^>]*>')
	detail=re_h.sub('',detail)
	ret = {}
	ret['jobName']=jobArr[0][0]
	ret['jobLink']=jobArr[0][1]
	ret['feedBack']=feedBack[0]
	ret['comLink']=comArr[0][0]
	ret['comName']=comArr[0][1]
	ret['salary']=jobSalary[0]
	ret['place']=jobPlace[0]
	ret['releaseDate']=releaseDate[0]
	ret['detail']=detail
	arrRet = [jobArr[0][0],jobArr[0][1],feedBack[0],comArr[0][0],comArr[0][1],jobSalary[0],jobPlace[0],releaseDate[0],detail]
	return ret,arrRet


def parsePage(pageNum):
	path = filePath + str(pageNum) + ".html"
	data =  readFile(path).replace('\n','').replace('\r','')
	retDic,res= parse(data)
	retDic['pageNum']=pageNum
	res['pageNum']=pageNum
	return retDic,res


def saveCSV(path,dataSet):
	with open(path,'w') as f:
		writer = csv.DictWriter(f,fieldnames=dataSet['head'])
		writer.writeheader()
		writer.writerows(dataSet['baseInfo'])
	f.close()


retDict,res=parsePage(1)
print(retDict['baseInfo'])
saveCSV('F:\codeGitBook\爬虫\图片爬虫\智联/1.csv',retDict)
#print(data)
#arr = [('href="http://company.zhaopin.com/%E8%81%94%E8%BF%AA%E6%81%92%E6%98%9F%28%E5%8D%97%E4%BA%AC%29%E4%BF%A1%E6%81%AF%E7%B3%BB%E7%BB%9F%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_CC143646990.htm"', '南京联迪信息系统股份有限公司')]
#print(arr[0][1])


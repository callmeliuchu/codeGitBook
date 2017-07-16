import re
import urllib.request
import os
import csv
filePath = "F:\codeGitBook\爬虫\数据爬虫\智联/"
def saveFile(filePath,data):
	with open(filePath,'wb') as f:
		f.write(data)

def readFile(filePath):
	with open(filePath,'rb') as f:
		return f.read().decode('utf-8')
#爬数据源,根据网页的页数，语言，城市来定位资源
def crawPage(pageNum,city,job):
	path = filePath+city + "/" + job + "/resource"
	if not os.path.exists(path):
		os.makedirs(path)
	path = path + "/"+ str(pageNum)+".html"
	if os.path.isfile(path):
		return
	url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl="+urllib.request.quote(city)+"&kw="+job+"&sm=0&p="+str(pageNum)
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	saveFile(path,data)
	data = str(data)
	print(data)

def readHtml(pageNum,city,job):
	path = filePath+ city + "/" + job + "/resource/"+str(pageNum)+".html"
	print(path)
	if not os.path.isfile(path):
		return
	return readFile(path)


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
	patCom = "<td class=\"gsmc\"><a href=\"(http://.*?)\".*?>(.*?)</a>"
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
	jobName = ""
	jobLink = ""
	feedBack = ""
	comName = ""
	comLink = ""
	salary = ""
	place = ""
	releaseDate = ""
	if len(jobArr)==1:
		jobName = jobArr[0][1]
		jobLink = jobArr[0][0]
	if len(feedBack)==1:
		feedBack = feedBack[0]
	if len(comArr)==1:
		comName = comArr[0][1]
		comLink = comArr[0][0]
	if len(jobSalary)==1:
		salary = jobSalary[0]
	if len(jobPlace)==1:
		place = jobPlace[0]
	if len(releaseDate)==1:
		releaseDate = releaseDate[0]
	ret['jobName']=jobName
	ret['jobLink']=jobLink
	ret['feedBack']=feedBack
	ret['comLink']=comLink
	ret['comName']=comName
	ret['salary']=salary
	ret['place']=place
	ret['releaseDate']=releaseDate
	ret['detail']=detail
	arrRet = [jobName,jobLink,feedBack,comLink,comName,salary,place,releaseDate,detail]
	return ret,arrRet


def parsePage(pageNum,city,job):
	path = filePath + city + "/" + job + "/resource/"+str(pageNum) + ".html"
	data =  readFile(path).replace('\n','').replace('\r','').replace(u'\xa0', u' ') 
	retDic,res= parse(data)
	retDic['pageNum']=pageNum
	res['pageNum']=pageNum
	return retDic,res


def saveCSV(path,head,content):
	if os.path.isfile(path):
		return
	with open(path,'w') as f:
		writer = csv.DictWriter(f,fieldnames=head)
		writer.writeheader()
		writer.writerows(content)
	f.close()


def saveDataByPageNum(pageNum,city,job):
	retDict,res=parsePage(pageNum,city,job)
	path = filePath + city +"/" + job + "/result_csv"
	if not os.path.exists(path):
		os.makedirs(path)
	path = path + "/" + str(pageNum) + ".csv"
	saveCSV(path,retDict['head'],retDict['baseInfo'])


def genDataByCrawlPage(city,job):
	crawPage(1,city,job)
	data = readHtml(1,city,job)
	patPageCounts = "zlapply.searchjob.enter2Page\(this,event,(.*?)\)"
	counts = re.compile(patPageCounts).findall(data)[0]
	print(counts)
	num = int(counts)
	for i in range(2,num+1):
		crawPage(i,city,job)
	for i in range(1,num+1):
		try:
			saveDataByPageNum(i,city,job)
		except Exception as e:
			print(str(e))


def searchCityJob():
	cities = ['上海']
	jobs = ['python','java','C++']
	for city in cities:
		for job in jobs:
			genDataByCrawlPage(city,job)

searchCityJob()



import urllib.request
import os
from bs4 import BeautifulSoup

def saveFile(path,data):
	with open(path,"wb") as f:
		f.write(data)
		f.close()


def readFile(path):
	with open(path,'rb') as f:
		data = f.read()
		f.close()
		return data.decode('utf8')


def readFileByCityJob(language,city,num):
	path = 'data/'+city+'/'+language+'/'+str(num) + '.html'
	data = readFile(path)
	return data



def crawlUrl(url,city,language,fileName):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	path = 'data/'+city+'/'+language
	print(path)
	if not os.path.exists(path):
		os.makedirs(path)
	filePath = path + "/" + fileName
	print(filePath)
	saveFile(filePath,data)

def crwalIndexHtml():
	url = "http://www.zhipin.com/"
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	saveFile("data/index.html",data)
	print(data.decode('utf8'))



def crawlCityAndJob(language,city):
	url = 'http://www.zhipin.com/job_detail/?query='+language+'&scity='+urllib.request.quote(city)+'&source=2'
	crawlUrl(url,city,language,"1.html")


# crawlCityAndJob("python","上海")
data = readFileByCityJob("python","上海",1)
print(data)
soup = BeautifulSoup(data,'lxml')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)
# print(soup.li)
# print(soup.p['class'])
# print(soup.find_all('li'))
joblist = soup.find('div',class_='job-list')
print(joblist)
joblist
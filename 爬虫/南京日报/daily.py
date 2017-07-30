import re
import urllib.request
import os
import csv
from FileDeal import *
filePath = "F:\codeGitBook\爬虫\南京日报/htmldata/"
# def saveFile(filePath,data):
# 	with open(filePath,'wb') as f:
# 		f.write(data)

#清除html标签
def delTag(data):
	re_h=re.compile('</?\w+[^>]*>')
	return re_h.sub('',data)	

# def readFile(filePath):
# 	with open(filePath,'rb') as f:
# 		return f.read().decode('utf-8')

#按照每一页抓取页面数据
def crawPage(pageNum):
	url = 'http://app.njdaily.cn/?app=search&controller=index&action=search&type=all&wd=%E5%81%87%E5%86%92%E4%BC%AA%E5%8A%A3&Submit=&page='+str(pageNum)+'&order=rel'
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	# path = filePath + "1.html"
	# saveFile(path,data)
	data = data.decode('utf8')
	# print(data)
	return data

#解析出一条新闻，主要用正则，磊磊你可以试试BeautifulSoup解析
def oneNewData(aNew):
	titlePat = "target=\"_blank\">(.*?)</a></dt><dd "
	title = re.compile(titlePat).findall(aNew)[0]
	descPat = "class=\"info\">(.*?)</dd><dd>"
	desc = re.compile(descPat).findall(aNew)[0]
	newsLinkPat = "<a href=\"(.*?)\""
	newsLink = re.compile(newsLinkPat).findall(aNew)[0]
	datePat = "<span class=\"green\">(.*?) </span>"
	date = re.compile(datePat).findall(aNew)[0]
	title = delTag(title)
	desc = delTag(desc)
	date = delTag(date)
	newsLink = delTag(newsLink)
	return {"title":title,"desc":desc,"date":date,"link":newsLink}


def collectDataByPage(aNewList,content):
	for news in aNewList:
		oneNew = oneNewData(news)
		content.append(oneNew)
		print(oneNew)

#解析出一页所有新闻
def parsePage(data,content):
	newsPat = "<div id=\"search_list.*?</div>"
	news = re.compile(newsPat).findall(data)[0]
	oneNewPat = "<dl>.*?</dl>"
	aNewList = re.compile(oneNewPat).findall(news)
	collectDataByPage(aNewList,content)



# def saveCSV(path,head,content):
# 	# if os.path.isfile(path):
# 	# 	return
# 	with open(path,'w',newline='') as f:
# 		writer = csv.DictWriter(f,fieldnames=head)
# 		writer.writeheader()
# 		writer.writerows(content)
# 	f.close()

# data = readFile(filePath + "1.html").replace('\n','').replace('\r','').replace(u'\xa0', u' ').replace("\t","")
# newsPat = "<div id=\"search_list.*?</div>"
# news = re.compile(newsPat).findall(data)
# # print(news[0])
# oneNewPat = "<dl>.*?</dl>"
# aNewList = re.compile(oneNewPat).findall(news[0])
# aNew = aNewList[0]
# titlePat = "target=\"_blank\">(.*?)</a></dt><dd "
# title = re.compile(titlePat).findall(aNew)[0]
# descPat = "class=\"info\">(.*?)</dd><dd>"
# desc = re.compile(descPat).findall(aNew)[0]
# newsLinkPat = "<a href=\"(.*?)\""
# newsLink = re.compile(newsLinkPat).findall(aNew)[0]
# datePat = "<span class=\"green\">(.*?) </span>"
# date = re.compile(datePat).findall(aNew)[0]
# print(oneNewData(aNew))
# print()
# print(aNew)
# printDataByPage(aNewList)
# parsePage(data)

#清除页面上换行等字符，主要是换行影响用正则，磊磊你可以试试BeautifulSoup解析
def cleanData(data):
	return data.replace('\n','').replace('\r','').replace(u'\xa0', u' ').replace("\t","")



def crawlData():
	#content列表收集所有数据
	content = []
	for pageNum in range(1,101):
		try:
			data = crawPage(pageNum)
			data = cleanData(data)
			parsePage(data,content)
			print(content)
		except Exception as e:
			print(str(e))
	path = "F:\codeGitBook\爬虫\南京日报/" + "data.csv"
	head=["title","desc","date","link"]
	with open(path,'w',newline='') as f:#存入csv
		writer = csv.DictWriter(f,fieldnames=head)
		writer.writeheader()
		for anew in content:#可能有些数据因为编码问题不能存入，用try catch忽略
			try:
				writer.writerow(anew)
			except Exception as e:
				print(str(e))


if "__main__" == __name__:
	crawlData()
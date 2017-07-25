import urllib.request
from FileDeal import *
import time
from bs4 import BeautifulSoup
from collections import deque
filePath="F:\codeGitBook\爬虫\电影天堂爬取\Data/"
startUrl = "http://www.dytt8.net"

def crawl(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	# path = filePath + htmlName + ".html"
	# saveFile(path,data)
	return  data.decode('gbk')


def getUrls(data):
	urls = set()
	soup = BeautifulSoup(data,'html.parser')
	for link in soup.find_all('a'):
		url  = link.get('href')
		if url == "#":
			continue
		if  url.startswith('/'):
			url = startUrl + url
		yield url



# data = readFile("F:\codeGitBook\爬虫\电影天堂爬取\Data/index.html")
# soup = BeautifulSoup(open("F:\codeGitBook\爬虫\电影天堂爬取\Data/index.html"),'html.parser')
# print(soup.prettify())
# print(soup.title)
 # print(soup.head)


def crawlUrls():
	urls = set()
	queue = deque()
	queue.append(startUrl)
	urls.add(startUrl)
	while len(queue)!=0:
		url = queue.popleft()
		try:
			data = crawl(url)
		except Exception as e:
			print(e)
		for aUrl in getUrls(data):
			if aUrl not in urls:
				time.sleep(0.01)
				print(aUrl)
				urls.add(aUrl)
				queue.append(aUrl)

# crawlUrls()
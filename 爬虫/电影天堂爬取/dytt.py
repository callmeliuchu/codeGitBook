import urllib.request
from FileDeal import *
from bs4 import BeautifulSoup


def crawl(url,filePath="F:\codeGitBook\爬虫\电影天堂爬取\Data/"):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	path = filePath + "index.html"
	saveFile(path,data)
	return  data.decode('gbk')


data = readFile("F:\codeGitBook\爬虫\电影天堂爬取\Data/index.html")
soup = BeautifulSoup(open("F:\codeGitBook\爬虫\电影天堂爬取\Data/index.html"),'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
for link in soup.find_all('a'):
	print(link.get('href'))

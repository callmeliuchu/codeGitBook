from FileDeal import *
import urllib.request



def crawl(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	# path = filePath + "index.html"
	# saveFile(path,data)
	return data.decode('utf-8')
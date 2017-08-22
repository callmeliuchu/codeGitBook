import urllib.request



def crwalIndexHtml():
	url = "http://blog.sina.com.cn/s/article_sort_1191258123_10001_1.html"
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	print(data.decode('utf8'))

crwalIndexHtml()
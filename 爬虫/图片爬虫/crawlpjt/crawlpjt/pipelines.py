# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class CrawlpjtPipeline(object):
	def process_item(self, item, spider):
		for i in range(len(item['picurl'])):
			url = item['picurl'][i][0]
			picid = item['picid'][i][0]
			try:
				kurl = url
				location = "F:/codeGitBook/爬虫/图片爬虫/mmpic/" +str(i)+picid+ ".jpg"
				urllib.request.urlretrieve(kurl,filename=location)
			except urllib.error.URLError as e:
				print(kurl+str(e))
		return item

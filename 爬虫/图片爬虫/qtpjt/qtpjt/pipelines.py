# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

class QtpjtPipeline(object):
	def process_item(self, item, spider):
		for i in range(len(item['picurl'])):
			picid = item['picid'][i]
			picurl = item['picurl'][i]
			trueurl = picurl + "_1024.jpg"
			location = "F:/codeGitBook/爬虫/图片爬虫/picture/"+picid+".jpg"
			urllib.request.urlretrieve(trueurl,filename=location)
		return item

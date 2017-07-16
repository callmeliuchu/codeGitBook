# -*- coding: utf-8 -*-
import scrapy
import re
from qtpjt.items import QtpjtItem

class QtspdSpider(scrapy.Spider):
    name = "qtspd"
    allowed_domains = ["58pic.com"]
    start_urls = ('http://www.58pic.com/topic/421-1.html',)

    def parse(self, response):
    	item = QtpjtItem()
    	paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
    	item['picurl']=re.compile(paturl).findall(str(response.body))
    	patid = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
    	item['picid']=re.compile(patid).findall(str(response.body))
    	yield item
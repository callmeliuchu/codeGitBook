# -*- coding: utf-8 -*-
import scrapy
from crawlpjt.items import CrawlpjtItem
from scrapy.http import Request
import re

class SmartspiderSpider(scrapy.Spider):
	name = "smartspider"
	allowed_domains = ["mmjpg.com"]
	start_urls = ['http://www.douluo123.com/shaonvmanhua/114220.html']

	def parse(self, response):
		item = CrawlpjtItem()
		paturl = "(http://dlpic.fungood.cn/uploads/.*?\.(jpg|png))"
		item['picurl'] = re.compile(paturl).findall(str(response.body))
		patid =   "http://dlpic.fungood.cn/uploads/.*?/(.*?)\.(jpg|png)"
		item['picid']=re.compile(patid).findall(str(response.body))
		yield item
		for i in range(201,220):
			url = "http://www.douluo123.com/shaonvmanhua/114" + str(i) + ".html"
			yield Request(url,callback=self.parse)

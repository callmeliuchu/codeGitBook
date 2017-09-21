import urllib.request
from bs4 import BeautifulSoup
import re
url = 'http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=jjcc&code=001740&topline=100&year=2017&month=2'
# data = urllib.request.urlopen(url).read().decode('utf-8')
# print(data)


class ttjj:
	def __init__(self,url):
		data = urllib.request.urlopen(url).read().decode('utf-8')
		data = re.compile('content:"(.*?)",arryear').findall(data)[0]
		# print(data)
		soup = BeautifulSoup(data,"html.parser")
		content = soup.select('table[class="w782 comm tzxq"]')[0]
		# print(content)
		self.head = content.select('thead')[0]
		self.body = content.select('tbody')[0]
		# print(self.body)
		self.desc = ['seq','code_info','name_info','new_price','raise_down','info','ratio_domain','code_owns','money_owns']
		self.columns = []
		self.parse_columns()
		self.rows = []
		self.parse_row()
		print(len(self.rows))
		for row in self.rows:
			for key in row:
				print(key,":",row[key])

		# print(body)
	def parse_columns(self):
		for column in self.head.select('th'):
			self.columns.append(column.get_text())
		# print(self.columns)
# ['序号', '股票代码', '股票名称', '最新价', '涨跌幅', '相关资讯', '占净值比例', '持股数（万股）', '持仓市值（万元）']
	def parse_row(self):
		for tr in self.body.select('tr'):
			tds = tr.select('td')
			seq = tds[0].get_text()
			code = tds[1].get_text()
			code_link = tds[1].select('a')[0].get('href')
			code_info = (code,code_link)
			name = tds[2].get_text()
			name_link = code_link
			name_info = (name,name_link)
			new_price = tds[3].get_text()
			raise_down = tds[4].get_text()
			info_a_arr = tds[5].select('a')
			info_arr = []
			for a in info_a_arr:
				content = a.get_text()
				link = a.get('href')
				info_arr.append((content,link))
			ratio_domain = tds[6].get_text()
			code_owns = tds[7].get_text()
			money_owns = tds[8].get_text()
			row = {'seq':seq,'code_info':code_info,'name_info':name_info,
			        'new_price':new_price,'raise_down':raise_down,'info':info_arr,
			        'ratio_domain':ratio_domain,'code_owns':code_owns,'money_owns':money_owns
			       }
			self.rows.append(row)
		# print(self.rows)








t_obj = ttjj(url)

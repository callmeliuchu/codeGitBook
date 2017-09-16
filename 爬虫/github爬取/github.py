import urllib.request
import os
from bs4 import BeautifulSoup
import re
import time
import csv
user_base_path = 'user_data'
csv_data_path = 'csv_data'

def save_file(path,data):
	with open(path,'wb') as f:
		f.write(data)
		f.close()

def read_file(path):
	with open(path,'rb') as f:
		return f.read().decode()

def get_tab_dic():
	return  {'repositories':'repositories','stars':'stars','followers':'followers','following':'following'}

class CSVTool:
	def __init__(self,path,file_name):
		self.path = path
		self.file_name = file_name
		self.writer = None
		self.init_writer()

	def insert_user(self,user):
		self.writer.writerow(user.get_data_arr())

	def get_read_rows(self):
		return csv.reader(open(self.path+'/'+self.file_name,'r',newline='',encoding= 'utf_8_sig'))




	def insert_users(self,users):
		for user in users:
			self.insert_user(user)

	def init_writer(self):
		if not os.path.exists(self.path):
			os.makedirs(self.path)
		path = self.path+'/'+self.file_name
		if os.path.exists(path):
			return
		self.writer = csv.writer(open(self.path+'/'+self.file_name,'w',newline='',encoding= 'utf_8_sig'))

	def close_session(self):
		self.writer.close()

class User:
	def __init__(self,html):
		self.dom = BeautifulSoup(html,'html.parser')
		self.base_url = 'https://github.com'
		self.tab_dic = {'repositories':'repositories','stars':'stars','followers':'followers','following':'following'}
		self.parse_base()
		self.addition_dic = {}
		self.addition_dic_parse()
		self.parse_addition_parse()
		self.profile = []
		self.profile_parse()
		self.following_arr = []
		self.parse_following()

	def parse_base(self):
		self.name = self.dom.select('span[itemprop="name"]')[0].get_text()
		self.url_name = self.dom.select('span[itemprop="additionalName"]')[0].get_text()
		try:
			self.bio = self.dom.select('div[class="p-note user-profile-bio"]')[0].get_text()
		except Exception as e:
			self.bio = ""
		try:
			self.location = self.dom.find_all(attrs={"aria-label":"Home location"})[0].get_text().strip()
		except Exception as e:
			self.location = ""

	def addition_dic_parse(self):
		for key,value in self.tab_dic.items():
			self.addition_dic[key] = ('/'+self.url_name+'?tab='+value)
		
	def trim_data(self,data):
		return data.replace('\n','').replace(' ','')


	def parse_addition_parse(self):
		self.repositories = self.dom.select('a[href="'+self.addition_dic['repositories']+'"]')[0].get_text()
		self.repositories = self.trim_data(self.repositories)
		self.stars = self.dom.select('a[href="'+self.addition_dic['stars']+'"]')[0].get_text().strip()
		self.stars  = self.trim_data(self.stars )
		self.followers = self.dom.select('a[href="'+self.addition_dic['followers']+'"]')[0].get_text().strip()
		self.followers = self.trim_data(self.followers)
		self.following = self.dom.select('a[href="'+self.addition_dic['following']+'"]')[0].get_text().strip()
		self.following = self.trim_data(self.following)


	def profile_parse(self):
		self.profile.append(self.name)
		self.profile.append(self.url_name)
		self.profile.append(self.bio)
		self.profile.append(self.location)
		self.profile.append(self.repositories)
		self.profile.append(self.stars)
		self.profile.append(self.followers)
		self.profile.append(self.following)

	def parse_following(self):
		following_dom = self.dom.select('div[class="position-relative"]')[0]
		following_dom_arr = following_dom.select('div[class="d-table col-12 width-full py-4 border-bottom border-gray-light"]')
		for dom in following_dom_arr:
			a_dom = dom.find('a')
			self.following_arr.append(a_dom.get('href')[1:])

	def get_following_arr(self):
		return self.following_arr


	def get_self_url(self):
		return self.base_url+"/"+self.url_name

	def get_self_name(self):
		return self.name

	def get_url_name(self):
		return self.url_name

	def get_data_arr(self):
		vec = self.profile[:]
		vec.append(','.join(self.following_arr))
		return vec

	def  __str__(self):
		return ",".join(self.profile)+'/'+','.join(self.get_following_arr())

def get_user(user_name,tab):
	url = "https://github.com/"+user_name+"?tab="+tab
	path = user_base_path + "/" + user_name + ".html"
	if not os.path.exists(path):
		data = urllib.request.urlopen(url).read()
		save_file(path,data)
		return data.decode()
	else:
		return read_file(path)

def clean_data(data):
	return data.replace("\n","").replace("\t","")



class Graph:
	def __init__(self,name,limit=2):
		self.dic =  {'repositories':'repositories','stars':'stars','followers':'followers','following':'following'}
		self.users = []
		self.visited = set([])
		self.deep_first(name,0,limit)

	def get_users(self):
		return self.users
		

	def deep_first(self,name,depth,limit):
		if depth >= limit:
			return
		self.visited.add(name)
		user_following = get_user(name,self.dic['following'])
		user = User(user_following)
		following_arr = user.get_following_arr()
		self.users.append(user)
		for following in following_arr:
			if following not in self.visited:
				self.visited.add(following)
				self.deep_first(following,depth+1,limit)

	def braedth_first(self,name,breadth_limit):
		queue = []
		queue.append(name)
		self.visited.add(name)
		count_breadth = 0
		while len(queue)!=0 and count_breadth < breadth_limit:
			size = len(queue)
			count_breadth = count_breadth + 1
			for i in range(size):
				pop_name = queue.pop(0)
				user_content = get_user(pop_name,self.dic['following'])
				user = User(user_content)
				following_arr = user.get_following_arr()
				print(user)
				for following in following_arr:
					if following not in self.visited:
						self.visited.add(following)
						queue.append(following)



class Graph_CSV:
	def __init__(self,start_name,data_arr):
		self.table = {}
		self.init_table(data_arr)
		self.visited = set([])
		self.path = []
		self.deep_first(start_name)

	def init_table(self,data_arr):
		for vec in data_arr:
			head = vec[0]
			sub_arr = vec[1]
			if head not in self.table:
				self.table[head] = []
			self.table[head].extend(sub_arr)

	def deep_first(self,name):
		self.visited.add(name)
		self.path.append(name)
		if name in self.table:
			next_users = self.table[name]
		else:
			return
		for user_name in next_users:
			if user_name not in self.visited:
				self.deep_first(user_name)

	def get_path(self):
		return self.path





	def get_table(self):
		return self.table


def get_csv_data():
	ret = []
	tool = CSVTool(csv_data_path,'users.csv')
	rows = tool.get_read_rows()
	for row in rows:
		head = row[1]
		if len(row[-1])==0:
			sub_arr = []
		else:
			sub_arr = row[-1].split(',')
		ret.append([head,sub_arr])
	return  ret


	# graph = Graph("callmeliuchu",5)
	# users = graph.get_users()
	# tool.insert_users(users)
	# print(os.listdir('user_data'))
	# print(len(os.listdir('user_data')))

data = get_csv_data()
graph_csv = Graph_CSV('callmeliuchu',data)
print(graph_csv.get_path())
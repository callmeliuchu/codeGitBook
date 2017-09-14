import urllib.request
import os
from bs4 import BeautifulSoup
import re
user_base_path = 'user_data'

def save_file(path,data):
	with open(path,'wb') as f:
		f.write(data)
		f.close()

def read_file(path):
	with open(path,'rb') as f:
		return f.read().decode()

# repositories
# stars
# followers
# following

def get_tab_dic():
	return {'repo':'repositories','starts':'starts','followers':'follower','following':'following'}



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

	def parse_base(self):
		self.name = self.dom.select('span[itemprop="name"]')[0].get_text()
		self.url_name = self.dom.select('span[itemprop="additionalName"]')[0].get_text()
		self.bio =  self.dom.select('div[class="p-note user-profile-bio"]')[0].get_text()
		self.location = self.dom.find_all(attrs={"aria-label":"Home location"})[0].get_text().strip()

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

	def get_self_url(self):
		return self.base_url+"/"+self.url_name

	def  __str__(self):
		return ",".join(self.profile)	





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


dic = get_tab_dic()
# print(dic['following'])
user_following = get_user('callmeliuchu',dic['following'])
user = User(user_following)
print(user)
# soup = BeautifulSoup(user_following,"html.parser")
# dom = soup
# # print(user_following)
# name = dom.select('span[itemprop="name"]')[0].get_text()
# url_name = dom.select('span[itemprop="additionalName"]')[0].get_text()
# bio_dom =  dom.select('div[class="p-note user-profile-bio"]')[0].get_text()
# location = dom.find_all(attrs={"aria-label":"Home location"})[0].get_text().strip()




# print(name)
# print(url_name)
# print(bio_dom)
# print(location)

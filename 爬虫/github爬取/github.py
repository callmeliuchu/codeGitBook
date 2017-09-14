import urllib.request
import os
from bs4 import BeautifulSoup
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
		self.html = html

	def parse(self):
		self.following = ''





def get_user(user_name,tab):
	url = "https://github.com/"+user_name+"?tab="+tab
	path = user_base_path + "/" + user_name + ".html"
	if not os.path.exists(path):
		data = urllib.request.urlopen(url).read()
		save_file(path,data)
		return data.decode()
	else:
		return read_file(path)



dic = get_tab_dic()
# print(dic['following'])
user_following = get_user('callmeliuchu',dic['following'])
soup = BeautifulSoup(user_following,"html.parser")
print(soup)
# print(user_following)

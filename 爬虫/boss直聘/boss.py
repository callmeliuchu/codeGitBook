import urllib.request
import os
import re
from bs4 import BeautifulSoup
from mysql_db import DB
import json
import useragent
import random
user_agent_arr = useragent.get_agent_arr()
default_header = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
is_write = False
# ['condition-city']  location
# ['condition-experience'] years
# ['condition-education'] education
# ['condition-scale'] comscale
# ['condition-stage'] finance
# ['condition-insdustry'] comdomain
# ['condition-salary'] jobsalary
# {"location":job_location,"years":job_years,"joblink":job_link,
# 	"jobdesc":job_desc,"jobsalary":job_desc,
# 	"education":job_edu,"comlink":com_link,"comname":com_name,
# 	"comdomain":com_domain,"finance":com_finance,"comscale":com_scale}


def writeJson(path,data):
	if os.path.isfile(path):
		return
	with open(path,'w') as f:
		json.dump(data,f)

def readJson(path):
	with open(path,'r') as f:
		dic = json.load(f)
		return dic




def saveFile(path,data):
	with open(path,"wb") as f:
		f.write(data)
		f.close()


def readFile(path):
	with open(path,'rb') as f:
		data = f.read()
		f.close()
		return data.decode('utf8')


def readFileByCityJob(language,city,num):
	path = 'data/'+city+'/'+language+'/'+str(num) +"/"+str(num)+'.html'
	data = readFile(path)
	return data



def crawlUrl(url,city,language,pagenum,filename,header=default_header):
	req = urllib.request.Request(url)
	req.add_header("User-Agent",header)
	data = urllib.request.urlopen(req).read()
	path = 'data/'+city+'/'+language+"/"+str(pagenum)
	print(path)
	if not os.path.exists(path):
		os.makedirs(path)
	filePath = path + "/" + filename+".html"
	if is_write:
		saveFile(filePath,data)
	else:
		if not os.path.isfile(path):
			saveFile(filePath,data)

def crwalIndexHtml():
	url = "http://www.zhipin.com/"
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')
	data = urllib.request.urlopen(req).read()
	saveFile("data/index.html",data)
	print(data.decode('utf8'))



def crawlCityAndJob(language,city,pagenum,header):
	# url = 'http://www.zhipin.com/job_detail/?query='+language+'&scity='+urllib.request.quote(city)+'&source=2'
	url = geturl(('城市',city),language)+"&page="+str(pagenum)+"&ka=page-"+str(pagenum)
	crawlUrl(url,city,language,pagenum,str(pagenum),header)


# crawlCityAndJob("python","上海")
# data = readFileByCityJob("python","上海",1)
# # print(data)
# soup = BeautifulSoup(data,'lxml')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.parent.name)
# # print(soup.li)
# # print(soup.p['class'])
# # print(soup.find_all('li'))
# joblist = soup.find('div',class_='job-list')
# # print(joblist)
# jobs= joblist.find_all('li')
# job= jobs[0]
def get_job_detail(job):
	job_primary = job.find_all('div',class_='job-primary')[0]
	job_tags = job.find_all('div',class_='job-tags')[0]
	job_time = job.find_all('div',class_='job-time')[0]
	# print(job_primary)
	# print(job_tags)
	# print(job_time)
	info_primary = job_primary.find_all('div',class_='info-primary')[0]
	job_dom = info_primary.find_all('a')[0]
	job_link = job_dom.get('href')
	job_content = str(job_dom)
	# print(job_content)
	# print(job_link)
	job_desc = re.compile('"_blank">(.*?)<span').findall(job_content)[0]
	# print(job_desc)
	job_salary = re.compile('red">(.*?)</span').findall(job_content)[0]
	# print(job_salary)
	job_require = str(info_primary.find_all('p')[0]).replace('<em class="vline"></em>',',')
	job_location,job_years,job_edu = re.compile('<p>(.*?)</p>').findall(job_require)[0].split(',')
	# print(job_location,job_years,job_edu)
	info_company = job_primary.find_all('div',class_='info-company')[0]
	com_link_dom = info_company.find_all('a')[0]
	com_link = com_link_dom.get('href')
	# print(com_link)
	com_name = com_link_dom.get_text()
	com_detail = str(info_company.find_all('p')[0]).replace('<em class="vline"></em>',',')
	try:
		com_domain,com_finance,com_scale = re.compile('<p>(.*?)</p>').findall(com_detail)[0].split(',')
	except Exception as e:
		com_domain,com_finance = re.compile('<p>(.*?)</p>').findall(com_detail)[0].split(',')
		com_scale = ""

	# print(com_domain,com_finance,com_scale)
	return {"location":job_location,"years":job_years,"joblink":job_link,
	"jobdesc":job_desc,"jobsalary":job_desc,
	"education":job_edu,"comlink":com_link,"comname":com_name,
	"comdomain":com_domain,"finance":com_finance,"comscale":com_scale}

# for job in jobs:
# 	job_detail = get_job_detail(job)
# 	joblink = job_detail['joblink']
# 	comname = job_detail['comname']
# 	url = "http://www.zhipin.com"+joblink
# 	crawlUrl(url,"上海","python","1_"+comname+".html")
# 	print()
def crawlMoreDetail(job_detail,city,language,num):
	joblink = job_detail['joblink']
	comname = job_detail['comname']
	url = "http://www.zhipin.com"+joblink
	crawlUrl(url,city,language,num,str(num)+"_"+comname)	


def readJobDetail(job_detail,city,language,num):
	joblink = job_detail['joblink']
	comname = job_detail['comname']
	path = "data"+"/"+city +"/"+language+"/"+str(num)+"/"+str(num)+"_"+comname+".html"
	data = readFile(path)
	soup = BeautifulSoup(data,'lxml')
	jobmoredetail = soup.find_all('div',class_='job-sec')[0].get_text().replace("\n","")
	print(comname,jobmoredetail)
	return jobmoredetail


def crawlDetailHTML(language,city,num,header):
	data = readFileByCityJob(language,city,num)
	print(data)
	soup = BeautifulSoup(data,'lxml')
	joblist = soup.find('div',class_='job-list')
	print(joblist)
	jobs= joblist.find_all('li')
	for job in jobs:
		try:
			jobdetail = get_job_detail(job)
			print(jobdetail)
			joblink = jobdetail['joblink']
			comname = jobdetail['comname']
			url = "http://www.zhipin.com"+joblink
			crawlUrl(url,city,language,num,str(num)+"_"+comname,header)
		except Exception as e:
			print(e)

def crawlPageByOne(language,city,num,header=default_header):
	crawlCityAndJob(language,city,num,header)
	crawlDetailHTML(language,city,num,header)	



# readJobDetail("","","","")
def parse(language,city,num):
	db = DB()
	table_name = "com_info"
	db.clear(table_name)
	data = readFileByCityJob(language,city,num)
	soup = BeautifulSoup(data,'lxml')
	joblist = soup.find('div',class_='job-list')
	jobs= joblist.find_all('li')
	for job in jobs:
		try:
			jobdetail = get_job_detail(job)
			jobmoredetail=readJobDetail(jobdetail,city,language,num)
			jobdetail['moredetail']=jobmoredetail
			jobdetail['city']=city
			jobdetail['language']=language
			db.insert(table_name,jobdetail)
			print(jobdetail)
		except Exception as e:
			print(e)


# crawlPageByOne("python","上海",1)
# parse("python","上海",1)
# ['condition-city']  location
# ['condition-experience'] years
# ['condition-education'] education
# ['condition-scale'] comscale
# ['condition-stage'] finance
# ['condition-insdustry'] comdomain
# ['condition-salary'] jobsalary
def mapping():
	cstodb = {}
	cstodb['condition-city'] = 'location'
	cstodb['condition-experience'] = 'years'
	cstodb['condition-education'] = 'education'
	cstodb['condition-scale'] = 'comscale'
	cstodb['condition-stage'] = 'finance'
	cstodb['condition-insdustry'] = 'comdomain'
	cstodb['condition-salary'] = 'jobsalary'
	return cstodb


def write_searchmap():
	# if os.path.isfile('searchmap.json'):
	# 	return
	data = readFileByCityJob("python","上海",1)
	soup = BeautifulSoup(data,'lxml')
	conditions = soup.find_all('div',class_='condition-box')[0]
	condition_arr = conditions.find_all('dl')
	csmapping = mapping()
	searchmap = {}
	for con in condition_arr:
		csdesc = con.get('class')[0]
		cscndesc = con.find_all('dt')[0].get_text().replace('：','')
		if csdesc in csmapping:
			dbdesc = csmapping[csdesc]
			adoms = con.find_all('a')
			dic = {}
			for adom in adoms:
				acontent = adom.get_text()
				# aka = adom.get('ka')
				alink = adom.get('href')
				if alink.startswith('/'):
					dic[acontent]=alink
					# print(acontent,alink)
			searchmap[cscndesc]=dic
			# print(cscndesc,csdesc,csmapping[csdesc])
	writeJson('searchmap.json',searchmap)


def read_searchmap():
	dic = readJson('searchmap.json')
	return dic

# 经验:['3-5年', '不限', '应届生', '5-10年', '1年以内', '1-3年', '10年以上']
# 规模:['20-99人', '1000-9999人', '0-20人', '10000人以上', '100-499人', '500-999人', '不限']
# 融资:['不限', '不需要融资', '天使轮', '已上市', 'D轮及以上', 'B轮', 'C轮', 'A轮', '未融资']
# 薪资:['15-20k', '20-30k', '5-10k', '30-50k', '不限', '50k以上', '3-5k', '3k以下', '10-15k']
# 学历:['博士', '本科', '高中', '中专及以下', '硕士', '不限', '大专']
# 行业:['生活服务', 'O2O', '移动互联网', '房地产/建筑', '汽车', '社交网络', '游戏', '供应链/物流', '咨询/翻译/法律', '分类信息', '非互联网行业', '旅游', '公关会展', '健康医疗', '广告营销', '文化娱乐', '电子商务', '信息安全', '金融', '企业服务', '不限', '采购/贸易', '网络招聘', '数据服务', '教育培训', '智能硬件', '媒体', '互联网', 'IT软件', '通信']
# 城市:['全国', '成都', '天津', '广州', '北京', '苏州', '上海', '西安', '武汉', '深圳', '长沙', '杭州', '厦门']

def geturl(items,language):
	searchmap = read_searchmap()
	item0 = items[0]
	item1 = items[1]
	return "http://www.zhipin.com"+searchmap[item0][item1].replace('python',language)


def get_rand_agent():
	return random.choice(user_agent_arr)


print(get_rand_agent())
language = 'C++'
city = '广州'
url = geturl(('融资','D轮及以上'),language)
crawlPageByOne(language,city,1,get_rand_agent())
parse(language,city,1)
# write_searchmap()
# searchmap = read_searchmap()
# for item in searchmap:
# 	print(item+":"+str(list(searchmap[item].keys())))
# http://www.zhipin.com/c101020100/?query=java&page=2&ka=page-2
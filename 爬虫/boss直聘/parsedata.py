from mysql_db import DB
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif']=['SimHei']
plt.style.use('ggplot')


def genpic():
	db = DB()
	table_name="com_info"
	res = db.query(table_name)
	fig = plt.figure(figsize=(15,15))
	fig.set(alpha=0.5)
	df = pd.DataFrame(res)
	print(df)
	plt.subplot2grid((2,2),(0,0))
	df.years.value_counts().plot(kind='bar')
	print(df.years.value_counts())
	plt.subplot2grid((2,2),(0,1))
	df.comscale.value_counts().plot(kind='bar')
	plt.subplot2grid((2,2),(1,0))
	df.education.value_counts().plot(kind='bar')
	plt.subplot2grid((2,2),(1,1))
	df.comdomain.value_counts().plot(kind='bar')
	plt.savefig('counts.jpg')  
	plt.show()	



if __name__=="__main__":
	counts = ['3-5年', '不限', '应届生', '5-10年', '1年以内', '1-3年', '10年以上']
	db = DB()
	table_name="com_info"
	res = db.query(table_name)
	for info in res:
		print(info['moredetail'])
	

	# for infos in res:
	# 	print(infos['years'])
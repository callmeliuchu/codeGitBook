import pymysql
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root")
conn1=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mydb2",port=3306,charset="utf8")



def exexute(insertSql):
	conn1.query("set character_set_client=gbk;")
	conn1.query("set character_set_results=gbk;")
	cs = conn1.cursor()
	val=cs.execute(insertSql)
	conn1.commit()



def createDB():
	val=conn.query("create database huajiao")
	print(val)
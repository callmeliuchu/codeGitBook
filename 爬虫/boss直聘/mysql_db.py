#coding=utf-8 
from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser


base_dir = str(os.path.dirname(__file__))
base_dir = base_dir.replace("\\","/")
file_path = base_dir + "/db_config.ini"
print(file_path)

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
db = cf.get("mysqlconf","db_name")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")
print(host,port,db,user,password)


class DB:
	def __init__(self):
		try:
			self.conn = connect(
				      host=host,
				      user=user,
				      password=password,
				      db=db,
				      charset='utf8',
				      cursorclass=cursors.DictCursor
				    )
		except OperationalError as e:
			print('mysqlError %d:%s'%(e.args[0],e.args[1]))

	def clear(self,table_name):
		real_sql = "delete from "+table_name +";"
		with self.conn.cursor() as cursor:
			cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
			cursor.execute(real_sql)
		self.conn.commit()

	def insert(self,table_name,table_data):
		for key in table_data:
			table_data[key] = "'" + str(table_data[key]) + "'"
		key = ','.join(table_data.keys())
		value = ','.join(table_data.values())
		real_sql = "INSERT INTO "+ table_name + "(" + key + ") VALUES ("+value+")"
		print(real_sql)
		with self.conn.cursor() as cursor:
			cursor.execute(real_sql)
		self.conn.commit()

	def query(self,table_name):
		real_sql = "SELECT * FROM "+table_name
		print(real_sql)
		with self.conn.cursor() as cursor:
			cursor.execute(real_sql)
			rows = cursor.fetchall()
			return rows

	def close(self):
		self.conn.close()


if __name__=="__main__":
	db = DB()
	table_name = "com_info"
	# data = {'education': '不限', 'comname': '武汉佰钧成', 'comlink': '/gongsi/106990.html', 'moredetail': '职位描述                            项目简介：    1、benchmark测试框架     主要对天基集群上部署的如pangu、nuwa、fuxi等服务进行自动化测试。其中包括机器上下线、磁盘上下线、集群扩缩容、服务升级等测试内容。    负责模块：pangu自动化测试框架的开发与维护。python岗位要求：－编写python相关工具，从事python测试相关代码编写－熟悉linux相关环境－测试也有可能涉及到web框架 比如测试report，但是不是主要focus－熟练掌握Python，熟悉python异步IO；－熟悉一种web开发框架，不限于Django/Flask/Tornado；－熟悉一种常用的python模版框架，不限于yaml和jinjia2；－熟悉一种常用的ORM框架，不限于 peewee/SQLAlchemy；－熟悉一种常用的消息队列框架，不限于Celery/RabbitMQ/ZeroMQ；－熟悉大规模集群的管理工具，不限于fabric／chef／salt；－有web开发经验，了解html、css、javascript等前端开发语言，熟悉但不限于jquery、angularjs、emberjs、extjs等常见js开发框架；                            ', 'jobsalary': 'Python开发 ', 'location': '北京', 'comscale': '10000人以上', 'jobdesc': 'Python开发 ', 'joblink': '/job_detail/1413639133.html', 'finance': '不需要融资', 'comdomain': 'IT软件', 'years': '1-3年'}
	# db.clear(table_name)
	# db.insert(table_name,data)
	infos = db.query(table_name)[0]
	for key,value in infos.items():
		print(str(key)+":"+str(value))
	db.close()

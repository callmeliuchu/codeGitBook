import pymysql




class mysql_init(object):
	def __init__(self,conn):
		self.conn = None

	def connect(self):
		self.conn = pymysql.connect(
			host = 'localhost',
			port = 3306,
			user = 'root',
			passwd = 'root',
			db = 'boss',
			charset='utf8'
		)

	def cursor(self):
		try:
			return self.conn.cursor()
		except(AttributeError,pymysql.OperationalError):
			self.connect()
			return self.conn.cursor()

	def commit(self):
		return self.conn.commit()


	def close(self):
		return self.conn.close()


def process():
	dbconn.connect()
	conn = dbconn.cursor()
	DropTable(conn)
	CreateTable(conn)
	InsertDatas(conn)
	QueryData(conn)
	dbconn.commit()
	dbconn.close()


def query(sql,conn):
	conn.execute(sql)
	rows = conn.fetchall()
	return rows

def DropTable(conn):
	conn.execute("DROP TABLE IF EXISTS `user_key`")

def CreateTable(conn):
	sql_create = '''DROP TABLE IF EXISTS `boss`;  
	CREATE TABLE `com_info` (  
	`id` int(11) NOT NULL AUTO_INCREMENT,  
	`comlink` varchar(60) NOT NULL,
	`finance` varchar(60) NOT NULL,
	`joblink` varchar(60) NOT NULL,
	`location` varchar(60) NOT NULL,
	`jobdesc` varchar(60) NOT NULL,
	`years` varchar(60) NOT NULL,
	`education` varchar(60) NOT NULL,
	`jobsalary` varchar(60) NOT NULL,
	`comscale` varchar(60) NOT NULL,
	`comname` varchar(60) NOT NULL,
	`comdomain` varchar(60) NOT NULL, 
	`moredetail` longtext NOT NULL, 
	`city` varchar(60) NOT NULL,
	`language` varchar(60) NOT NULL, 
	  PRIMARY KEY (`id`)  
     ) ENGINE=MyISAM  DEFAULT CHARSET=utf8;  
	                '''
	conn.execute(sql_create)


def InsertDatas(conn):
	insert_sql = "INSERT INTO user_key VALUES (%(value)s)"
	key_list = ["你好","恩恩"]
	conn.executemany(insert_sql,[dict(value=v) for v in key_list])

def DeleteData(conn):
	del_sql = "delete from user_key where id=2"
	coon.execute(del_sql)

def QueryData(conn):
	sql = "select * from user_key"
	rows = query(sql,conn)
	printResult(rows)

def printResult(rows):
	if rows is None:
		print('row is none')
		return
	for row in rows:
		print(row)

def getStr(val):
	return "`"+val+"` varchar(60) NOT NULL,"

if __name__ =="__main__":
	columns = ['comlink', 'finance', 'joblink', 'location', 'jobdesc', 'years', 'education', 'jobsalary', 'comscale', 'comname', 'comdomain']
	for column in columns:
		print(getStr(column))
	
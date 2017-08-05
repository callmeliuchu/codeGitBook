import sys
sys.path.append("../db_fixture")
from  mysql_db  import DB


datas = {
	"sign_event":[
	        {"id":1,"name":"xiaomi","`limit`":2000,"status":1,"address":"center",
	        "start_time":"2016-08-20 00:25:42","create_time":"2016-08-20 00:25:42"},
 	        {"id":2,"name":"ewfewf","`limit`":2000,"status":1,"address":"center",
	        "start_time":"2016-08-20 00:25:42","create_time":"2016-08-20 00:25:42"},             
	        {"id":3,"name":"dfdsfs","`limit`":2000,"status":1,"address":"center",
	        "start_time":"2016-08-20 00:25:42","create_time":"2016-08-20 00:25:42"},
	        {"id":4,"name":"dfdsfsqwe","`limit`":2000,"status":1,"address":"center",
	        "start_time":"2016-08-20 00:25:42","create_time":"2016-08-20 00:25:42"},
	        ],
	"sign_guest":[
            {"id":1,"realname":"alen","phone":1355554501,"email":"alen@qq.com",
            "sign":0,"event_id":1,"create_time":"2016-08-20 00:25:42"},
            {"id":2,"realname":"alen","phone":135555345201,"email":"alen@qq.com",
            "sign":0,"event_id":1,"create_time":"2016-08-20 00:25:42"},
            {"id":3,"realname":"alen","phone":13555234501,"email":"alen@qq.com",
            "sign":0,"event_id":1,"create_time":"2016-08-20 00:25:42"},
            {"id":4,"realname":"alen","phone":13555432501,"email":"alen@qq.com",
            "sign":0,"event_id":1,"create_time":"2016-08-20 00:25:42"},
	],
}




def init_data():
	db = DB()
	for table,data in datas.items():
		db.clear(table)
		for d in data:
			db.insert(table,d)
	db.close()


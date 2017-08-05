from pymysql import cursors,connect

conn = connect(
       host='127.0.0.1',
       user='root',
       password='root',
       db='guest_test',
       charset='utf8mb4',
       cursorclass=cursors.DictCursor
	)

try:
	with conn.cursor() as cursor:
		
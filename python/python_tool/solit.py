
s = "C_UNIT_CODE=BOCOFFICE,C_BK_GROUP_ID=BOC,C_PRODUCT_ID=P12081400004,C_PRODUCT_NAME=出口托收直联业务,C_ITEM_ID=Release,C_FUNC_ID=F05030701131,C_LOCKED_FLAG=F,T_LOCKED_TIME=,SMS_CONTENT=null"
arr = s.split(",")
res = []
res1 = []
for ele in arr:
	id = '"'+ele.split('=')[0]+'"'
	id1 = ele.split('=')[0]
	res.append(id)
	res1.append(id1)
print(",".join(res))
print(','.join(res1))

# jsonStr={%27OP1%27%EF%BC%9A%272017-09-14%27;%27OP2%27%EF%BC%9A%272017-09-16%27;%27OP7%27%EF%BC%9A%2725460023%27;}
# s = "%27OP1%27%EF%BC%9A%272017-09-14%27;%27OP2%27%EF%BC%9A%272017-09-16%27;%27OP7%27%EF%BC%9A%2725460023%27"
# print(s.replace("%27",","))

from bs4 import BeautifulSoup
import os
def split_int_sql(s):
	# s = "C_UNIT_CODE=BOCOFFICE,C_BK_GROUP_ID=BOC,C_PRODUCT_ID=P12081400004,C_PRODUCT_NAME=出口托收直联业务,C_ITEM_ID=Release,C_FUNC_ID=F05030701131,C_LOCKED_FLAG=F,T_LOCKED_TIME=,SMS_CONTENT=null"
	arr = s.split(',')
	vec = []
	for ele in arr:
		vec.append("'"+ele.split('=')[1]+"'")
	return ','.join(vec)
# C_UNIT_CODE=BOCOFFICE,C_BK_GROUP_ID=BOC,C_PRODUCT_ID=P12081400004,C_PRODUCT_NAME=出口托收直联业务,C_ITEM_ID=Release,C_FUNC_ID=F05030701131,C_LOCKED_FLAG=F,T_LOCKED_TIME=,SMS_CONTENT=null

# s="""
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# 	<business type = "create" desc="经办业务通知" id="P08071500000">
# 	  <ID>F05030700965</ID>
# 	  <ID>F05030700977</ID>
# 	  <ID>F05030700978</ID>
# 	  <ID>F05030700903</ID>
# 	</business>
# 	<business type = "release" desc="授权业务通知" id="P11021600000">
# 	  <ID>F05030700800</ID>
# 	  <ID>F05030700988</ID>
# 	  <ID>F05030700802</ID>
# 	  <ID>F05030701067</ID>
# 	</business>
# 	<business type = "document" desc="单证信息通知">
# 	  <ID>F05030700700</ID>
# 	  <ID>F05030700993</ID>
# 	  <ID>F05030700702</ID>
# 	  <ID>F05030700703</ID>
# 	</business>
# </root>
# """
# print(s)


    # <product hasAuth="N" type="S">
    #     <id>P13040900000</id>
    #     <name>BocInqCompany</name>
    #     <desc>客户信息查询</desc>
    #     <module>SECU</module>
    # </product>
    # <product hasAuth="N" type="S">
    #     <id>P11032100001</id>
    #     <name>Document Maintain</name>
    #     <desc>帮助文档维护</desc>
    #     <module>SECU</module>
    # </product>
    # <product hasAuth="N" type="S">
    #     <id>P11031400001</id>
    #     <name>BankOperator FAP Maintain</name>
    #     <desc>银行网点操作员权限维护</desc>
    #     <module>SECU</module>
    # </product>
    # <product hasAuth="N" type="S">
    #     <id>P11031400000</id>
    #     <name>Bank Operator Maintain</name>
    #     <desc>银行网点操作员维护</desc>
    #     <module>SECU</module>
    # </product>

# C_UNIT_CODE=BOCOFFICE,C_BK_GROUP_ID=BOC,
# C_PRODUCT_ID=P12081400004,C_PRODUCT_NAME=出口托收直联业务,
# C_ITEM_ID=Release,C_FUNC_ID=F05030701131,C_LOCKED_FLAG=F,T_LOCKED_TIME=,SMS_CONTENT=null
def parse_func_root():
	prd_dic = {"P13040900000":"客户信息查询","P11032100001":"帮助文档维护","P11031400000":"银行网点操作员维护"}
	path = 'C:\liuchusoftware\liuchusoftware\BOC\EnvironmentBOC/backupparameteter\PARAM\BOC\CN\AP\FUNC/function_root.xml'
	base_sql = 'INSERT INTO "CEUSER"."STT_SMS_INFO" (C_UNIT_CODE,C_BK_GROUP_ID,C_PRODUCT_ID,C_PRODUCT_NAME,C_ITEM_ID,C_FUNC_ID,C_LOCKED_FLAG,T_LOCKED_TIME,SMS_CONTENT)'+\
    'VALUES '
	with open(path,encoding='utf-8') as f:
		soup = BeautifulSoup(f.read(),"html.parser")
		funclist = soup.find_all()[1:]
		for func in funclist:
			func_desc = func.get('desc')
			func_type = func.get('functype')
			func_id = func.get('id')
			func_item = func.get('item')
			module_desc = func.get('moduledesc')
			product_id = func.get('product')
			if product_id in prd_dic:
				s = "C_UNIT_CODE=BOCOFFICE,C_BK_GROUP_ID=BOC,C_PRODUCT_ID="+product_id+",C_PRODUCT_NAME="+\
				prd_dic[product_id]+",C_ITEM_ID="+func_item+",C_FUNC_ID="+func_id+",C_LOCKED_FLAG=F,T_LOCKED_TIME=,SMS_CONTENT=null"
				# print(func_desc,func_type,func_id,func_item,module_desc,product_id,prd_dic[product_id])
				# print(s)
				values = '('+split_int_sql(s)+')'
				sql = base_sql + values+";"
				print(sql)
		# for func in funclist:
		# 	print(func)
		# print(len(funclist))

		# print(help(soup))

parse_func_root()
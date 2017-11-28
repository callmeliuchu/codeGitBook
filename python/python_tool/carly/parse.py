import csv
from bs4 import BeautifulSoup
import os

# <type value="11-4" name="ATA单证册保函">
# 	<IMG_TYPE isMandory="Y">申办ATA单证册付款通知单</IMG_TYPE>
# 	<IMG_TYPE>ATA单证册申请表</IMG_TYPE>
# 	<IMG_TYPE>其他资料（如需）</IMG_TYPE>
# </type>

# <set default="" disp="申请书" value="申请书"/>
def get_temp(mark,name,content_arr,mandory_num):
	s = "<type value=\""+mark+"\" name=\""+name+"\">"
	for i in range(len(content_arr)):
		if i in mandory_num:
			s = s + "<IMG_TYPE isMandory=\"Y\">"+content_arr[i]+"</IMG_TYPE>"
		else:
			s = s + "<IMG_TYPE>"+content_arr[i]+"</IMG_TYPE>"
	return s + "</type>"










options = \
"""
<option value="11-4">ATA单证册保函</option>
<option value="11-2">一般关税保函</option>
<option value="6-5">付款保函（付款期限≤1年）</option>
<option value="6-1">付款保函（付款期限＞1年）</option>
<option value="2-1">借款/透支保函</option>
<option value="6-2">公用事业保函</option>
<option value="11-7">其它税款保函</option>
<option value="2-3">其它融资性保函</option>
<option value="16-7">其它非融资性保函</option>
<option value="6-3">农民工工资支付保函</option>
<option value="11-6">出口退税保函</option>
<option value="11-1">加工贸易税款保付保函</option>
<option value="6-4">国内工程项下业主支付保函</option>
<option value="16-4">对外劳务合作备用金保函</option>
<option value="9-1">履约保函</option>
<option value="7-1">投标保函</option>
<option value="16-2">提单遗失保函</option>
<option value="16-8">无船承运业务经营者保证金保函</option>
<option value="2-4">有价证券保付保函</option>
<option value="11-8">汇总征税保函</option>
<option value="15-1">海事保函</option>
<option value="11-3">电子支付税费担保</option>
<option value="4-1">经营性租赁保函</option>
<option value="14-1">维修保函</option>
<option value="2-2">综合授信额度保函</option>
<option value="11-5">船舶吨税保函</option>
<option value="1-1">融资性租赁保函</option>
<option value="5-1">补偿贸易保函</option>
<option value="16-1">诉讼保函</option>
<option value="16-3">货运监管保函</option>
<option value="13-1">质量保函</option>
<option value="8-1">预付款保函</option>
<option value="10-1">预留金/留置金保函</option>"""

sys_chars = "1234一二"


def get_dic():
	soup = BeautifulSoup(options,"lxml")
	option = soup.find_all('option')
	ret_result = {}
	for op in option:
		ret_result[op.get_text()] = op.get('value')
	return ret_result



def conver_c(c):
	if c in '1234':
		return int(c)
	elif c=='一':
		return 1
	elif c=='二':
		return 2



def parse_csv(mydic):
	reader = csv.reader(open('document.csv', encoding='gbk'))
	next(reader)
	result = {}
	result_str = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><root>"
	for row in  reader:
		data = row[0]
		arr =  data.split('\t')
		try:
			seq = int(arr[0])
		except Exception as e:
			a = 1
		doctype = arr[1]
		content = arr[2]
		hasChose = arr[4]
		# print(arr)
		if len(content)!=0:	
			new_arr = [doctype,content,hasChose]
			if seq not in result:
				result[seq] = []
			result[seq].append(new_arr)
	for seq in result:
		arr = result[seq]
		doc_type = arr[0][0].strip()
		content = [vec[1][2:].strip() for vec in arr]
		has_chose = arr[0][2]
		choose_arr = []
		for c in has_chose:
			if c in sys_chars:
				choose_arr.append(conver_c(c))
		try:
			s_temp = get_temp(mydic[doc_type],doc_type,content,choose_arr)
			result_str = result_str + s_temp
			# print(doc_type,content,choose_arr,mydic[doc_type])
		except Exception as e:
			a = 1
			# print(e)
	return result_str+"</root>"

def write(file_name,content):
	with open(file_name,'w',encoding='utf8') as f:
		f.write(content)



mydic = get_dic()
st = parse_csv(mydic)
write('issue_immage_mapping.xml',st)

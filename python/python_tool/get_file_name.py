import os
import re


desc_func = "进口信用证信息查询&F05030700968,"+\
 "进口代收信息查询&F05030700973,"+\
 "出口信用证信息查询&F05030700960,"+\
 "出口托收信息查询&F05030700999,"+\
 "保函开立信息查询&F05030701000,"+\
 "保函通知信息查询&F05030701001,"+\
 "收费信息查询（保函开立）&F05030701007,"+\
 "福费廷业务信息查询&F05030701004"
maping = desc_func.split(',')
dic = {}
for vec in maping:
	arr = vec.split('&')
	dic[arr[1]] = arr[0]
print(maping)
target_files = "F05030700968,F05030700973,F05030700960,F05030700999,F05030701000,F05030701001,F05030701007,F05030701004".split(",")
func_file_path = "C:/liuchusoftware/liuchusoftware/BOC/EnvironmentBOC/BOC/CN/AP/FUNC"
cata_file_path = "C:/liuchusoftware/liuchusoftware/BOC/EnvironmentBOC/BOC/CN/WEB/CATA"
cata_code_file_path = "C:\liuchusoftware\liuchusoftware\BOC\EnvironmentBOC\codefile\BOC\CN\WEB\CATA"
svae_file_path = "C:\liuchusoftware\liuchusoftware\BOC\EnvironmentBOC/result_jsp"


def walk_file(root_path):
	count = 0
	for file in os.walk(root_path):
		return file

def read_file(path):
	with open(path,encoding='utf8') as f:
		return f.read()

def save_file(path,data):
	with open(path,'w',encoding='utf8') as f:
		f.write(data)
		f.close()

def get_jsps():
	ret_arr = []
	for file in target_files:
		file_name = "func_" + file + ".xml"
		file_path = func_file_path + "/" + file_name
		cont = read_file(file_path)
		cata_id = re.compile('<CATALOGID>(.*?)</CATALOGID>').findall(cont)[0]
		cata_path = cata_file_path + "/"+"cata_" + cata_id + ".xml"
		cata_cont = read_file(cata_path)
		jsp_file = re.compile('<JSPFILE TMPLFILE=".*?">(.*?)</JSPFILE>').findall(cata_cont)[0]
		ret_arr.append((file,jsp_file))
	return ret_arr
def get_total_cont(cont):
	cont = re.compile("<div.*?id=\"total\">(.*?)div>").findall(cont)
	if len(cont)>0:
		arr = re.compile("<TD(.*?)</TD>").findall(cont[0])
		return arr
	else:
		return "empty"




jsps = get_jsps()
print(jsps)
for funcId,jsp_name in jsps:
	cata_path = cata_code_file_path + "/" + jsp_name
	cont = read_file(cata_path)
	name = dic[funcId] + "_" + funcId + "_" + jsp_name + ".jsp" 
	save_file(svae_file_path+"/"+name,cont)
	print(jsp_name)




# root,_,file_names = walk_file(func_file_path)
# print(file_names)






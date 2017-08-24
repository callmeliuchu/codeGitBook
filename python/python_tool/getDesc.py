import re
from bs4 import BeautifulSoup

root = "E:/BOCPARALLEL_DO/CE_STD_V_2_5_1_BOC_DOMESTIC_PARALLEL/CE_STD_V_2_5_1_BOC_DOMESTIC_PARALLEL _SCRIPT/"
path =[
'CEWeb/WebContent/BOC/CN/WEB/CATA/EXCL_GeneralCatalog.jsp',
'CEWeb/WebContent/BOC/CN/WEB/CATA/EXLC_GeneralCatalog.jsp',
'CEWeb/WebContent/BOC/CN/WEB/CATA/IMCL_GeneralCatalog.jsp',
'CEWeb/WebContent/BOC/CN/WEB/CATA/IMLC_GeneralCatalog.jsp',
'CEWeb/WebContent/BOC/CN/WEB/CATA/LGAD_GeneralCatalog.jsp',
'CEWeb/WebContent/BOC/CN/WEB/CATA/LOFG_GeneralCatalog.jsp',
'CEWeb/WebContent/BOC/CN/WEB/CATA/NEGO_GeneralCatalog.jsp',
'CEWeb/WebContent/screen/SYS_CriteriaTran.jsp'
]

for file in path:
	fileName = file.split("/")[-1]
	with open(root+file,encoding='utf-8') as f:
		html = f.read()
		soup = BeautifulSoup(html,"html.parser")
		print(fileName,soup.find_all("td", class_="ListLabel"))

	
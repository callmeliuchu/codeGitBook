import re

s = "<[EXPIRY_PLC,LC_AMT,CUST_NO]>"
# index = s.startswith(s)
# print(index)
# print(s.replace("<[","").replace("]>",""))
res = re.compile("<\[(.*?)\]>").match(s).span()
print(res)
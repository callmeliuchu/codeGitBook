def is_chinese(uchar):
 
        """判断一个unicode是否是汉字"""
 
        if uchar >= u'/u4e00' and uchar<=u'/u9fa5':
 
                return True
 
        else:
 
                return False
 
def is_number(uchar):
 
        """判断一个unicode是否是数字"""
 
        if uchar >= u'/u0030' and uchar<=u'/u0039':
 
                return True
 
        else:
 
                return False
 
def is_alphabet(uchar):
 
        """判断一个unicode是否是英文字母"""
 
        if (uchar >= u'/u0041' and uchar<=u'/u005a') or (uchar >= u'/u0061' and uchar<=u'/u007a'):
 
                return True
 
        else:
 
                return False
 
def is_other(uchar):
 
        """判断是否非汉字，数字和英文字符"""
 
        if not (is_chinese(uchar) or is_number(uchar)):
 
                return True
 
        else:
 
                return False



with open('C:/Program Files/feiq/feiq.fql','r',encoding='gb18030', errors='ignore') as f:
	lines = f.readlines()
	for line in lines:
		s = [c for c in line if is_other(c)]
		print(''.join(s))
	# print(f.read())
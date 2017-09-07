import os

def walk_file(root_path):
	count = 0
	for file in os.walk(root_path):
		if len(file[2])>0:
			count = count + 1
			print(file)
	print(count)


walk_file('C:/liuchusoftware/liuchusoftware/文档/bruceSMS/codeBruce')




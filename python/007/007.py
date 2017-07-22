import os


def getLines(fileName):
	blankCount = 0
	commentCount = 0
	codeCount = 0
	count = 0
	tag = False#used to make sure it is comment beteen ''' and '''
	with open(fileName) as f:
		lines = f.readlines()
		count = len(lines)
		for line in lines:
			#line = line.strip()
			if(line.strip().startswith("'''")):
				if not tag:
					tag = True
				else:
					tag = False
					commentCount = commentCount + 1
					#print('comment:'+line)
			if tag:
				commentCount = commentCount + 1
				#print('comment:'+line)

			if(line.strip().startswith("#")):
				commentCount = commentCount + 1
				#print('comment:'+line)

			if line.strip() == "":
				blankCount = blankCount + 1
				#print("blank"+line)
		codeCount = count - commentCount - blankCount
	return [{'code':codeCount},{'comment':commentCount},{'blank':blankCount}]


fileName = "F:/anaconda\Anaconda\Scripts"

for file in os.listdir(fileName):
	if file.endswith('.py'):
		print(file)
		file = fileName + "/" + file
		print(getLines(file))




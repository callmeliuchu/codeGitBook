
fileName = "F:\codeGitBook\python/011/011.txt"

def getWords(fileName):
	words = []
	with open(fileName) as f:
		for line in f.readlines():
			data = line.strip()
			words.append(data)
	return words

def input_word(type_in):
	words = getWords(fileName)
	if type_in in words:
		print('freedom')
	else:
		print('human word')

input_word("sex")
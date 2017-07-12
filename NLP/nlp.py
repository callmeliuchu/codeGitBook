import re

#4-1 NLP
def get_text(file):
	text = open(file).read()
	text = re.sub('\s+',' ',text)
	text = re.sub(r'<.*?>',' ',text)
	return text


def tag(word):
	assert isinstance(word,str),'argument has to be string'
	if word in ['a','the','all']:
		return 'det'
	else:
		return 'None'


def testData():
	return ['take','care','of','yourself']

def extract_property(prop):
	data = testData()
	return [prop(w) for w in data]

def test():
	prop = lambda w : w[-1]
	prop1 = lambda x : len(x)
	print(extract_property(prop1))


def search1(substring,words):
	result = []
	for word in words:
		if substring in word:
			result.append(word)
	return result

def search2(substring,words):
	for word in words:
		if substring in word:
			yield word

def testSearch1():
	data = ['hello','world','and','anapple']
	print(search1('an',data))

def testSearch2():
	data = ['hello','world','and','anapple']
	for val in search2('an',data):
		print(val)

#全排列
def permutations(seq):
	if len(seq) <= 1:
		yield seq
	else:
		for perm in  permutations(seq[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + seq[0:1] + perm[i:]


#高洁函数
def  is_content_word(word):
	return word.lower() not in ['a','of','and','will',',','.']

def testFilter():
	sent = ['Take','care','will']
	res=filter(is_content_word,sent)
	res2 = [w for w in sent if is_content_word(w)]
	for val in res2:
		print(val)

def testMap():
	import nltk
	words = nltk.corpus.brown.sents(categories='news')
	length = list(map(len,words))
	length2 = [len(w) for w in words]
	print(length==length2)
	print(sum(length))


def repeat(msg='<empty>',num=1):
	return msg*num



def testRepeat():
	print(repeat(num=3,msg='hhhhhh'))

def generic(*arg,**kwargs):
	print(arg)
	print(kwargs)

def testgeneric():
	generic('f','h','j',monkey='kkkk')



def test():
	songs = [['hhhh','huuuu','ppppp'],
			['oooooo','iiiiii','kkkkkk'],
			['yyyyyy','tttttt','gggggg']]
	print(list(zip(songs[0],songs[1],songs[2])))
	print(list(zip(*songs)))

def location():
	import nltk
	print(nltk.metrics.__file__)

def  insert(trie,key,value):
	if key:
		first,rest=key[0],key[1:]
		if first not in trie:
			trie[first]={}
		insert(trie[first],rest,value)
	else:
		trie['value']=value

def testTrie():
	import nltk
	trie = nltk.defaultdict(dict)
	insert(trie,'chat','cat')
	insert(trie,'chien','dog')
	insert(trie,'chair','flesh')
	insert(trie,'hic','stylish')
	print(trie)


import re
import nltk
def testFile():
	files = nltk.corpus.movie_reviews.abspaths()
	return files


def raw(file):
	contents = open(file).read()
	contents = re.sub(r'<.*?>',' ',contents)
	contents = re.sub('\s+',' ',contents)
	return contents


#排列组合
def snippet(doc,term):
	text = ' '*30 + raw(doc) + ' '*30
	pos = text.index(term)
	return text[:pos-30] + text[pos+30:]



#四种方法计算范文旋律：迭代，自底向上的动态规划，自上而下的动态规划，内置默记法
def virahanka1(n):
	if n==0:
		return [""]
	elif n==1:
		return ["S"]
	else:
		s = ["S" + prosody for prosody in virahanka1(n-1)]
		l = ["L" + prosody for prosody in virahanka1(n-2)]
		return s + l

def virahanka2(n):
	lookup = [[""],["S"]]
	for i in range(n-1):
		s = ["S" + prosody for prosody in lookup[i+1]]
		l = ["L" + prosody for prosody in lookup[i]]
		lookup.append(s + l)
	return lookup[n]


def virahanka3(n,lookup={0:[""],1:["S"]}):
	if n not in lookup:
		s = ["S" + prosody for prosody in virahanka3(n-1)]
		l = ["L" + prosody for prosody in virahanka3(n-2)]
		lookup[n] = s + l
	return lookup[n]

def virahanka4(n):
	if n==0:
		return [""]
	elif n==1:
		return ["S"]
	else:
		s = ["S" + prosody for prosody in virahanka4(n-1)]
		l = ["L" + prosody for prosody in virahanka4(n-2)]
		return s + l


def testVirahankval():
	list1 = virahanka1(4)
	list2 = virahanka2(4)
	list3 = virahanka3(4)
	list4 = virahanka4(4)
	print(list1)
	print(list2)
	print(list3)
	print(list4)

colors = 'rgbcmyk'
def bar_chart(categories,words,counts):
	import pylab
	ind = pylab.arange(len(words))
	width = 1 / (len(categories) + 1)
	bar_groups = []
	for c in range(len(categories)):
		bars  = pylab.bar(ind+c*width,counts[categories[c]],width,color=colors[c%len(colors)])
		bar_groups.append(bars)
	pylab.xticks(ind+width,words)
	pylab.legend([b[0] for b in bar_groups],categories,loc='upper left')
	pylab.ylabel('Frequency')
	pylab.title('frequency')
	pylab.show()





def testDraw():
	genres = ['news','religion','hobbies','government','adventure']
	modals = ['can','could','may','might','must','will']
	cfdist = nltk.ConditionalFreqDist(
		(genre,word)
		for genre in genres
		for word in nltk.corpus.brown.words(categories=genre)
		if word in modals
		)
	counts = {}
	for genre in genres:
		#counts[genre] = [cfdist[genre][word]]
		counts[genre]=[cfdist[genre][word] for word in modals]
	bar_chart(genres,modals,counts)



def testChapter5():
	text = nltk.word_tokenize('And now for something compeletely different')
	res = nltk.pos_tag(text)
	print(res)

testChapter5()
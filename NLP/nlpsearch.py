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

def snippet(doc,term):
	text = ' '*30 + raw(doc) + ' '*30
	pos = text.index(term)
	return text[:pos-30] + text[pos+30:]

print('begin ....')
#files = testFile()
#idx = nltk.Index((w,f) for f in files for w in raw(f).split())
#print(idx)
query = raw_input("query> ")
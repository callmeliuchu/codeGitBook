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



print(tag('the'))
print(tag('uuu'))


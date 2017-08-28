import pandas as pd


def readFile(path):
	with open(path,encoding='utf8') as f:
		return f.read()


training_variants_data = pd.read_csv('training_variants',sep=",")
test_variants_data = pd.read_csv('test_variants',sep=',')
train_text = readFile("F:/代码日记/training_text")
test_text = readFile("F:/代码日记/test_text")




print(training_variants_data)
print(test_variants_data)
print(train_text)
print(test_text)
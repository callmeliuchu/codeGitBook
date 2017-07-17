import json

def saveFile(filePath,data):
	with open(filePath,'wb') as f:
		f.write(data)

def readFile(filePath):
	with open(filePath,'rb') as f:
		return f.read().decode('utf-8')


def writeJson(file,data):
	with open(file, 'w') as f:
		json.dump(data, f)	

def readJson(file):
	with open(file, 'r') as f:
		data = json.load(f)
		return data
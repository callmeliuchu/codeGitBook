


with open('content.txt','rb') as f:
	dic = {}
	content = f.read().decode('utf-8')
	for word in content.split('，'):
		aWord = word.strip().replace(' ','').replace('\r|\n','')
		arr = aWord.split('（')
		try:
			chongLanguage = arr[0]
			chinese = arr[1].replace('）','')
		except Exception as e:
			new_arr = aWord.split('(')
			try:
				chongLanguage = new_arr[0]
				chinese = new_arr[1].replace(')','')
			except Exception as e:
				s = ''
		dic[chinese] = chongLanguage

print(dic)
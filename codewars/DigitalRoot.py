


def digital_root(n):
	if(n<10):
		return n
	vec = list(map(lambda x:int(x),list(str(n))))
	return digital_root(sum(vec))



print(digital_root(23654))

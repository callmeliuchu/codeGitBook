registry = []


def register(func):
	print('running register(%s)' % func)
	registry.append(func)
	return func


@register
def f1():
	print('running f1')



@register
def f2():
	print('running f2')



def f3():
	print('runing f3')




def main():
	print('runing main')
	print('register->',register)
	f1()
	f2()
	f3()



if __name__ == "__main__":
	main()
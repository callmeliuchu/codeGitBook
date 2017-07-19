import string
import random

KEY_LEN = 20
KEY_ALL = 200


def base_str():
	return string.ascii_letters + string.digits

def gen_key():
	key_list = [random.choice(base_str()) for i in range(KEY_LEN)]
	return ''.join(key_list)

def print_key(func):
	def _print_key(num):
		for i in func(num):
			print(i)
	return _print_key


@print_key
def key_num(num,result=None):
	if result ==  None:
		result = []
	for i in range(KEY_ALL):
		result.append(gen_key())
	return result



if __name__ == "__main__":
	key_num(KEY_ALL)
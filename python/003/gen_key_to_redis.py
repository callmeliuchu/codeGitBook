import string 
import random
import redis


base_str = string.ascii_letters  + string.digits


def generate_code(count,length):
	for i in range(count):
		s = ""
		for j in range(length):
			s = s + random.choice(base_str)
		yield s


def save_code():
	r = redis.Redis(host='127.0.0.1',port='6379')
	codes = generate_code(200,20)
	p = r.pipeline()
	for code in codes:
		p.sadd('code',code)
	p.execute()
	return r.scard('code')

if __name__ == '__main__':
	save_code()
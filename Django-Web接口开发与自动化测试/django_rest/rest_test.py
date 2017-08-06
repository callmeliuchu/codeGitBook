import unittest
import requests


class UserTest(unittest.TestCase):
	def setUp(self):
		self.base_url = 'http://localhost:8000/users'
		self.auth = ('admin','admin123456')

	def test_user1(self):
		r = requests.get(self.base_url+"/1/",auth=self.auth)
		result = r.json()
		print(result)
		self.assertEqual(result['username'],'admin')
		self.assertEqual(result['email'],'1371772034@qq.com')


class GroupTest(unittest.TestCase):
	def setUp(self):
		self.base_url = 'http://localhost:8000/groups'
		self.auth = ('admin','admin123456')

	def test_group1(self):
		r = requests.get(self.base_url+"/1/",auth=self.auth)
		result = r.json()
		print(result)
		self.assertEqual(result['name'],'test')


if __name__ == "__main__":
	unittest.main()

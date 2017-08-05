import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentdir)
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
	def setUp(self):
		self.base_url="http://localhost:8000/api/add_event/"

	def tearDown(self):
		print(self.result)

	def test_add_event_all_null(self):
		payload = {"eid":"","":"","limit":"","address":"","start_time":""}
		r = requests.post(self.base_url,data=payload)
		self.result = r.json()
		print(self.result)
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result['message'],'parameter error')

if __name__=="__main__":
	test_data.init_data()
	unittest.main()

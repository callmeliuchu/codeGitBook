import requests
import unittest

class GetEventListTest(unittest.TestCase):
	def setUp(self):
		self.url = "http://localhost:8000/api/get_event_list/"

	def test_get_event_null(self):
		r = requests.get(self.url,params={'eid':''})
		result = r.json()
		self.assertEqual(result['status'],10021)
		self.assertEqual(result['message'],"parameter error")


	def test_get_event_error(self):
		r = requests.get(self.url,params={'eid':'901'})
		result = r.json()
		self.assertEqual(result['status'],10022)
		self.assertEqual(result['message'],"query result is empty")


if __name__ == "__main__":
	unittest.main()
import time,sys
sys.path.append("./interface")
sys.path.append("./db_fixture")
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data


test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
print(discover)


if __name__ == "__main__":
	test_data.init_data()
	now = time.strftime('%Y-%m-%d %H-%M-%S')
	print(now)
	filename = './report/' + now + '_result.html'
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream=fp,title="Guest Manager Sytem interface test report",
	description='Implementation Example with:')
	runner.run(discover)
	fp.close()

# coidng=utf-8
from lexinyundong.pagedom.common import HTMLTestRunner
import  unittest,os,time
class Testone(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        '''不等于'''
        self.assertEqual(5,5)
    def test_02(self):
        self.assertEqual(6,1)
    def test_03(self):
        '''打印'''
        print (3)

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testone('test_01'))
    suit.addTest(Testone('test_02'))
    suit.addTest(Testone('test_03'))
    report_time=time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = os.path.dirname(__file__)+'/report/'+report_time+'result.html'
    print(report_path)
    with open(report_path,"wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='report',description='balabala')
        runner.run(suit)

from count import listto
import unittest, ddt
data = [{'list': [0], 'result': [0]},
        {'list': ["a"], 'result': False},
        {'list': [1, 1], 'result': [1, 1]},
        {'list': [1, 2], 'result': [2, 1]},
        {'list': [1, 2, 3], 'result': [2, 1, 3]},
        {'list': [1, 2, 3, '4'], 'result': False}]
@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.file_data('F:\\GitHub\\pydj\\first\\data_dic.yml')
    def test1(self, list, result):
        self.assertEqual(listto(list), result)

if __name__ == '__main__':
    unittest.main()
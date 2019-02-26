# coidng=utf-8
import unittest
from first.count import Calculator


class CountTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(1, 2)

    def tearDown(self):
        pass

    def test_add(self):
        r = self.cal.add()
        self.assertEqual(r, 3)

    def test_sub(self):
        r = self.cal.sub()
        self.assertEqual(r, -1)

    def test_mul(self):
        r = self.cal.mul()
        self.assertEqual(r, 2)

    def test_div(self):
        r = self.cal.div()
        self.assertEqual(r, 0.5)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CountTest("test_add"))
    suite.addTest(CountTest("test_div"))
    print (suite)
    runner = unittest.TextTestRunner()
    runner.run(suite)

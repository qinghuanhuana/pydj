from time import sleep
import unittest, random, sys
from model import myunit, function
from page_obj.loginPage import login
sys.path.append('./model')
sys.path.append('./page_obj')

class loginTest(myunit.MyTest):
    def user_login_verify(self, username='13662673020', password=''):
        login(self.dr).user_login(username, password)

    def test_login(self):
        self.user_login_verify()
        po = login(self.dr)
        try:
            self.assertEqual(po.user_error_hint(), '账号不能为空')
            self.assertEqual(po.pawd_error_hint(), '密码不能为空')
        except Exception as e:
            print('error %s' % e)
        finally:
            function.insert_img(self.dr, 'user_pawd_empty.png')


if __name__ == "__main__":
    unittest.main()

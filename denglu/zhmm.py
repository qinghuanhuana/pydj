# coidng=utf-8
import unittest, requests, os, sys, json, time
from requests.auth import HTTPBasicAuth
from denglu.ReadExecle import openExecle
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning
import HTMLTestRunner


class LoginRegister(unittest.TestCase):
    def setUp(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.openexecle = openExecle(r'.\Data\testcase.xlsx', 'test_denglu')
        self.headers = {"Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo X21i A Build/O11019)"}

    def tearDown(self):
        print(self.result)

    ''' 已注册号码 '''

    def test_zhuce_mobile(self):
        r = requests.post(self.openexecle.sheet.row(1)[3].value, data=self.openexecle.sheet.row(1)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(1)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(1)[8].value)

    ''' 未注册号码 '''

    def test_weizhuce_mobile(self):
        r = requests.post(self.openexecle.sheet.row(2)[3].value, data=self.openexecle.sheet.row(2)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(2)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(2)[8].value)

    ''' 图片验证码错误 '''

    def test_yzmerr_photo(self):
        r = requests.post(self.openexecle.sheet.row(3)[3].value, data=self.openexecle.sheet.row(3)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(3)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(3)[8].value)

    ''' 正确手机验证码 '''

    def test_yzmtrue_phone(self):
        r = requests.post(self.openexecle.sheet.row(4)[3].value, data=self.openexecle.sheet.row(4)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(4)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(4)[8].value)

    ''' 错误手机验证码 '''

    def test_yzmerr_phone(self):
        r = requests.post(self.openexecle.sheet.row(5)[3].value, data=self.openexecle.sheet.row(5)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(5)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(5)[8].value)

    ''' 重设密码 '''

    def test_reset_password(self):
        r = requests.post(self.openexecle.sheet.row(6)[3].value, data=self.openexecle.sheet.row(6)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(6)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(6)[8].value)

    ''' 已注册手机号注册 '''

    def test_registerBy_phone(self):
        r = requests.post(self.openexecle.sheet.row(7)[3].value, data=self.openexecle.sheet.row(7)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(7)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(7)[8].value)

    ''' 错误手机验证码注册 '''

    def test_yzmRegerr_phone(self):
        r = requests.post(self.openexecle.sheet.row(8)[3].value, data=self.openexecle.sheet.row(8)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(8)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(8)[8].value)

    ''' 未注册手机号注册 '''

    def test_registerNo_phone(self):
        r = requests.post(self.openexecle.sheet.row(9)[3].value, data=self.openexecle.sheet.row(9)[6].value,
                          headers=self.headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], self.openexecle.sheet.row(9)[7].value)
        self.assertEqual(self.result["msg"], self.openexecle.sheet.row(9)[8].value)

    """ 用户资料 """

    def test_register_user(self):
        from denglu.common.get_token import login, write_token
        from denglu.common.read_token import read_token
        url = self.openexecle.sheet.row(10)[3].value
        pram = self.openexecle.sheet.row(10)[6].value
        session, userid = login(url, pram)
        write_token(session)
        cookie = read_token()
        headers = {"Content-Type": "application/json; charset=utf-8",
                   "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo X21i A Build/O11019)",
                   "Host": "sports-qa.lifesense.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                   "Cookie": cookie}
        pram2 = {"userId": userid}
        base_url2 = "https://sports-qa.lifesense.com/user_service/getUserById?appType=6&clientId=40ddb066d7db4c7d93d2a7f14f8bdf3c&screenWidth=1080&screenHeight=2154&requestId=f68ac27ec1914728a4a145a4c2707ef4&systemType=2&version=3.5.2"
        r2 = requests.post(base_url2, json=pram2, headers=headers, verify=False)
        self.result = r2.json()
        userid = int(userid)
        self.assertEqual(self.result["code"], 200)
        self.assertEqual(self.result["msg"], u"成功")
        self.assertEqual(self.result["data"]["id"], userid)


if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(LoginRegister('test_registerBy_phone'))
    suit.addTest(LoginRegister('test_yzmtrue_phone'))
    suit.addTest(LoginRegister('test_yzmerr_phone'))
    report_time=time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = os.path.dirname(__file__)+'/report/'+report_time+'result.html'
    with open(report_path,"wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='report',description='balabala')
        runner.run(suit)
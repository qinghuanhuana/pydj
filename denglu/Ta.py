# coidng=utf-8
import unittest, requests, os, sys, json, time
from requests.auth import HTTPBasicAuth
from denglu.ReadExecle import openExecle
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning
import HTMLTestRunner
from denglu.common.sendMail import sendmail
from denglu.common.get_response import *


class ta_Case(unittest.TestCase):
    def setUp(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.openexecle = openExecle(r'.\Data\tacase.xlsx', 'test_denglu')
        self.headers = {"Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo X21i A Build/O11019)"}
        self.exturl = '&appType=1&tenant=tianan&'

    def tearDown(self):
        pass

    def test_login_true(self):
        url = self.openexecle.get_url()[1] + get_request_id()
        r = requests.post(url, json=json.loads(self.openexecle.get_pram()[1]))
        self.result = r.json()
        self.assertEqual(self.result['code'], self.openexecle.get_code()[1])
        self.assertEqual(self.result['msg'], self.openexecle.get_msg()[1])

    def test_login_false(self):
        url = self.openexecle.get_url()[2] + get_request_id()
        r = requests.post(url, json=json.loads(self.openexecle.get_pram()[2]))
        self.result = r.json()
        self.assertEqual(self.result['code'], self.openexecle.get_code()[2])
        self.assertEqual(self.result['msg'], self.openexecle.get_msg()[2])

    def test_sync_step(self):
        response = Response(self.openexecle.get_url()[1], self.openexecle.get_pram()[1])
        url = self.openexecle.get_url()[3] + response.get_token() + '&' + get_request_id()
        r = requests.post(url, json=json.loads(self.openexecle.get_pram()[3]))
        self.result = r.json()
        self.assertEqual(self.result['code'], self.openexecle.get_code()[3])
        self.assertEqual(self.result['msg'], self.openexecle.get_msg()[3])

    def test_step_activity(self):
        response = Response(self.openexecle.get_url()[1], self.openexecle.get_pram()[1])
        url = self.openexecle.get_url()[4] + response.get_token() + '&' + get_request_id()
        r = requests.post(url, json=json.loads(self.openexecle.get_pram()[4]))
        self.result = r.json()
        self.assertEqual(self.result['code'], self.openexecle.get_code()[4])
        self.assertEqual(self.result['msg'], self.openexecle.get_msg()[4])

    def test_find_activity_list(self):
        response = Response(self.openexecle.get_url()[1], self.openexecle.get_pram()[1])
        url = self.openexecle.get_url()[5] + response.get_token() + '&' + get_request_id() + self.exturl + response.get_userid()
        r = requests.post(url, json=json.loads(self.openexecle.get_pram()[5]))
        self.result = r.json()
        self.assertEqual(self.result['code'], self.openexecle.get_code()[5])
        self.assertEqual(self.result['msg'], self.openexecle.get_msg()[5])

    def test_find_point_detail(self):
        response = Response(self.openexecle.get_url()[1], self.openexecle.get_pram()[1])
        url = self.openexecle.get_url()[6] + response.get_token() + '&' + get_request_id() + self.exturl + response.get_userid()
        r = requests.post(url, json=json.loads(self.openexecle.get_pram()[6]))
        self.result = r.json()
        self.assertEqual(self.result['code'], self.openexecle.get_code()[6])
        self.assertEqual(self.result['msg'], self.openexecle.get_msg()[6])


if __name__ == "__main__":
    # suit = unittest.TestLoader().discover('.', 'Ta.py')
    suit = unittest.TestLoader().loadTestsFromTestCase(ta_Case)
    # suit.addTest(LoginRegister('test_'))
    report_time=time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = os.path.dirname(__file__)+'/report/'+report_time+'result.html'
    with open(report_path,"wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='report', description='balabala')
        runner.run(suit)
# coidng=utf-8
import requests, os, yaml
from ruamel import yaml
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning
from denglu.ReadExecle import openExecle
import random, string
class Response():
    def __init__(self, url, pram):
        self.url = url
        self.pram = pram
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        headers = {
            "Content-Type":"application/json; charset=utf-8",
            "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo X21i A Build/O11019)"
        }
        self.r = requests.post(self.url, data=self.pram, headers=headers, verify=False)

    def get_response(self):
        json = self.r.json()
        return json

    def get_token(self):
        token = self.get_response()["data"]["accessToken"]
        token = 'accessToken' + '=' + token
        return token

    def get_userid(self):
        userid = self.get_response()["data"]["userId"]
        userid = 'userId' + '=' + str(userid)
        return userid

    def get_saasUserid(self):
        saasUserid = self.get_response()["data"]["saasUserId"]
        saasUserid = 'saasUserId' + '=' + str(saasUserid)
        return saasUserid

def get_request_id():
    ran_str = ''.join(random.sample(string.ascii_lowercase + string.digits, 30))
    requestid = 'requestId' + '=' + ran_str
    return requestid

if __name__ == "__main__":
    readdata = openExecle(r'..\Data\tacase.xlsx', 'test_denglu')
    url = readdata.sheet.row(1)[3].value + get_request_id()
    pram = readdata.sheet.row(1)[6].value
    response = Response(url, pram)
    url1 = 'https://sports.lifesense.com/tianansp_service/stepActivity/falling?' + get_request_id() + '&' + response.get_token()
    a = requests.post(url1, json={"step": 2924, "userId": "3", "uploadTime": 1575339632519})
    print(a.json())


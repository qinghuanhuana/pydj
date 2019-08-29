# coidng=utf-8
import requests,json,urllib3
from urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
class reqs(object):
    def __init__(self,url, pram, fangshi):
        self.url = url
        self.pram = pram
        self.fangshi = fangshi

    def testapi(self):
        if self.fangshi == "POST":
            self.pram = json.loads(self.pram)
            urllib3.disable_warnings(InsecureRequestWarning)
            r = requests.post(self.url,json=self.pram,verify=False)
            json_response = json.loads(r.text)
            code = json_response["code"]
            return code, json_response

if __name__=="__main__":
    a=reqs("https://sports-qa.lifesense.com/sms_service/verify/send_code_v3?requestId=1000&sessionId=nosession",'{"code":"0zys","mobile":"13662673020"}','POST')
    print(a.testapi())


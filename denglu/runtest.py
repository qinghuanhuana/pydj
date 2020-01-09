# coidng=utf-8
from denglu.Fzqingqiu import reqs
from denglu.ReadExecle import openExecle
from denglu.HTMLTestRunner import HTMLTestRunner
from denglu.py_Html import createHtml
from denglu.common.sendMail import sendmail
import os,time,unittest,datetime
class Testinterface(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testinterface(self):
        self.data = openExecle(r".\Data\tacase.xlsx", "test_denglu")
        listpram = self.data.get_pram()
        listurl = self.data.get_url()
        listurl2 = self.data.get_url2()
        listmeth = self.data.get_meth()
        listcode = self.data.get_code()
        listmsg = self.data.get_msg()
        listid = self.data.get_id()
        listname = self.data.get_name()
        listresult = []
        listjson=[]
        list_pass = 0
        list_fail = 0
        list_url = []
        for i in range(len(listurl)):
            request = reqs(url=listurl[i]+listurl2[i], pram=listpram[i], fangshi=listmeth[i])
            code, json= request.testapi()
            if code == listcode[i] and json['msg'] == listmsg[i]:
                list_pass += 1
                listresult.append("pass")
                listjson.append(json)
            else:
                list_fail += 1
                listresult.append("fail")
                listjson.append(json)
            list_url.append(listurl[i] + listurl2[i])
        return list_fail, list_pass, listid, listname, list_url,listmeth, listpram, listcode, listmsg, listresult, listjson

if __name__ == "__main__":
    starttime = datetime.datetime.now()
    suit = unittest.TestSuite()
    me = Testinterface()
    list_fail,list_pass,listid,listname,list_url,listmeth,listpram,listcode,listmsg,listresult,listjson=me.testinterface()
    suit.addTest(Testinterface('testinterface'))
    report_time=time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = os.path.dirname(__file__)+'/report/'+report_time+'result.html'
    endtime = datetime.datetime.now()
    createHtml(titles='接口测试报告',
               filepath=report_path,passge=list_pass,fail=list_fail,starttime=starttime,endtime=endtime,
               id=listid,name=listname,url=list_url,meth=listmeth,pram=listpram,yuqi=listcode,json=listjson,relusts=listresult)

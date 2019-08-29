from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib, unittest, time, os

def send_mail(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtp.login('251064362@qq.com', 'oumyvqjxrrctcahd')
    smtp.sendmail('251064362@qq.com', 'xiu.yang@lifesense.com', msg.as_string())
    smtp.quit()

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new

if __name__ =='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './bbs/report/' + now + 'result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试执行情况')
        discover = unittest.defaultTestLoader.discover('./bbs/test_case/', pattern='*_sta.py')
        runner.run(discover)
    file_path = new_report('./bbs/report/')
    send_mail(file_path)
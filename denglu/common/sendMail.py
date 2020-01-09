# coidng=utf-8
import smtplib,time,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_setting():
    import yaml
    with open(r".\Data\email.yaml", "r") as fp:
        data = yaml.load(fp)
    return data["foremail"], data["password"], data["toeamil"], data["toemail"], data["port"]

def sendmail(file_path, neirong=''):
    from_addr, password, mail_to, smtpserver, smtpport=email_setting()
    neirong = input("please input your test name:")
    msg = MIMEMultipart()
    msg['Subject'] = u'接口自动化测试报告'
    msg['From'] =u'自动化测试平台'
    msg['To'] = mail_to
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    with open(file_path, 'rb') as fp:
        mail_body = fp.read()
    body = MIMEText(neirong, "html",'utf-8')
    att = MIMEText(mail_body, 'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(att)
    msg.attach(body)
    smtp = smtplib.SMTP_SSL(smtpserver,smtpport)
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, mail_to, msg.as_string())
    smtp.quit()
    print("邮件发送成功")

if __name__ == "__main__":
    sendmail("../Data/relult.html","yyy")
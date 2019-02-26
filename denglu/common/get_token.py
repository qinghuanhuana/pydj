# coidng=utf-8
import requests, os, yaml
from ruamel import yaml
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning
from denglu.ReadExecle import openExecle

def login(url,pram):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    headers = {
    "Content-Type":"application/json; charset=utf-8",
    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo X21i A Build/O11019)"
    }
    r = requests.post(url,data=pram,headers=headers,verify=False)
    session = r.headers["Set-Cookie"]
    json = r.json()
    userid= json["data"]["userId"]
    return session,userid

def write_token(session):
    curpath = os.path.dirname(os.path.dirname(__file__))
    ypath = os.path.join(curpath, "Data", "token.yaml")
    t = {"Cookie":session}
    with open(ypath, "w", encoding="utf-8") as f:
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)
if __name__=="__main__":
    readdata = openExecle(r'..\Data\testcase.xlsx')
    url = readdata.sheet.row(10)[3].value
    pram = readdata.sheet.row(10)[6].value
    print(login(url,pram))
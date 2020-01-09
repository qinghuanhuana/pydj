import requests,json
from random import random

url = 'https://sports-beta.lifesense.com/tiananuser_service/user/login?requestId=1804289383&osType=2'
header = {'Content-Type': 'application/json',
          'User-Agent': 'okhttp/3.12.0'
          }
data = {
  "agentCode": "100001169"
}
l = 0
for i in range(100001230, 100001240):
    data['agentCode'] = i
    r = requests.post(url=url,json=data,headers=header)
    json = r.json()
    l +=1
print(l)


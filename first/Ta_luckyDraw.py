# coding = utf-8
import requests
import json
youyang_one = 0
youyang_two = 0
lexin = 0
coffce = 0
maodanglao = 0
s11 = 0
mambo5 = 0
mambo = 0

for i in range(1000):
    url = 'https://sports-beta.lifesense.com/saasactivity_service/luckyWheel/luckyDraw?requestId=c5051a80ffaa11e9872a451bd44f6857&appType=1&tenant=tianan&userId=33220013 '
    data = {"loginId":"4518809","activityId":20}
    r = requests.post(url,json=data)
    # name = json.loads(r.text)['data']['prizeName']
    num = int(json.loads(r.text)['data']['prizeItemKey'])
    # print(name)
    if num == 1:
        youyang_one +=1
    elif num == 2:
        youyang_two +=1
    elif num == 454566:
        lexin +=1
    elif num == 216334:
        coffce +=1
    elif num == 544566:
        maodanglao +=1
    elif num == 989878:
        s11 +=1
    elif num == 678784:
        mambo5 +=1
    elif num == 6949512:
        mambo +=1
    else:
        print('不在奖品列表')

print(youyang_one, youyang_two, lexin, coffce, maodanglao, s11, mambo5, mambo)





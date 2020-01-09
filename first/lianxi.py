# coding=utf8
import random
print(random.random())
print(random.uniform(1, 2))
print(random.randint(1, 5))
def v_code():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randint(65, 90))
        add = random.choice([num, alf])
        code = ''.join([code, str(add)])
    return code
print(v_code())

import time
a = time.time()
print(a)
print(time.gmtime(a))
print(time.localtime(a))
print(time.strftime('%Y%m%d %X'))
print(time.ctime(a))
true_time = time.mktime(time.strptime('2017-09-11 08:30:00', '%Y-%m-%d %H:%M:%S'))
time_now = time.mktime(time.strptime('2017-09-12 11:00:00', '%Y-%m-%d %H:%M:%S'))
dif_time = time_now - true_time
struct_time = time.gmtime(dif_time)
print(struct_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))


from datetime import datetime
print(datetime.now())
print(datetime.utcnow())
print(datetime(2019, 10, 1, 22, 22, 22))
print(datetime.strptime('2017年9月30日星期六','%Y年%m月%d日星期六'))
print(datetime.strptime('2017年9月30日星期六8时42分24秒','%Y年%m月%d日星期六%H时%M分%S秒'))
print(datetime.now().strftime('%m%d'))

import json
f = open('file', 'w')
json.dump({'国籍':'中国'},f)
ret = json.dumps({'国籍':'中国'})
f.write(ret+'\n')
json.dump({'国籍':'美国'}, f, ensure_ascii=False)
ret = json.dumps({'国籍':'美国'}, ensure_ascii= False)
f.write(ret+'\n')
f.close()
data = {'username':['李华','二愣子'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
print(json_dic2)
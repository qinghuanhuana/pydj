# coidng=utf-8
import random, string
username = []
username= ''.join(random.sample(u'物联可穿戴赋能新医疗为主题参加了本届全国医院物联网大会',3))
print(username)

print(random.randrange(1,50))

ran_str = ''.join(random.sample(string.digits, 9))
print(int(ran_str))
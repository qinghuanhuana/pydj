# coidng=utf-8
import hashlib
import time
past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))
timearray = time.strptime(past_time,"%Y-%m-%d %H:%M:%S")
timestamp = int(time.mktime(timearray)*1000)
print (past_time,future_time,timestamp)
md5 = hashlib.md5()
mima="Igjz3due0uXDJRwT5dw63LI8ngfuTbpBhs3AR68X"
word_str = mima+str(timestamp)
print(word_str)
word_bytes_utf8 = word_str.encode(encoding='utf-8')
md5.update(word_bytes_utf8)
word_md5 = md5.hexdigest()
print(word_md5)


# import time
# a = time.time()
# print (a)
# print(int(a))
# print(int(round(a*1000)))
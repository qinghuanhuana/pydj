# coidng=utf-8
import time
import hashlib

'''当前时间'''
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

timearray = time.strptime(past_time, "%Y-%m-%d %H:%M:%S")

'''当前时间时间戳'''
timestamp = int(time.mktime(timearray) * 1000)

print (past_time, timearray, timestamp)

md5 = hashlib.md5()
word_str = "Igjz3due0uXDJRwT5dw63LI8ngfuTbpBhs3AR68X" + str(timestamp)
word_bytes_utf8 = word_str.encode(encoding='utf-8')
md5.update(word_bytes_utf8)
word_md5 = md5.hexdigest()
print(word_md5)
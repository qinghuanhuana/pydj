# coidng=utf-8
from time import sleep, ctime
import threading

def super_player(file_, time):
    for i in range(2):
        print('start playing: %s, %s' % (file_, ctime()))
        sleep(time)

lists = {'my love.mp3': 3, 'your like': 5, 'you and me': 4}
threads = []
files = range(len(lists))
for file_, time in lists.items():
    t = threading.Thread(target=super_player, args=(file_, time))
    threads.append(t)

if __name__ == '__main__':
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('time end: %s' % ctime())


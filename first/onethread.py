# coidng=utf-8
from time import sleep, ctime
def music(func, loop):
    for i in range(loop):
        print('listening to music %s %s' % (func, ctime()))
        sleep(2)

def movie(func, loop):
    for i in range(loop):
        print('looking to movie %s %s' % (func, ctime()))
        sleep(5)

if __name__ == '__main__':
    music('my love', 2)
    movie('your like', 2)
    print(ctime())
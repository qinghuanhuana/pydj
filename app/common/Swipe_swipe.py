# coidng=utf-8
import time
def get_size(dr):
    x = int(dr.get_window_size()['width'])
    y = int(dr.get_window_size()['height'])
    return x, y

'''向上滑'''
def swipe_up(dr, t=500, n=1):
    screen = get_size(dr)
    for i in range(n):
        dr.swipe(screen[0]*0.5,screen[1]*0.75,screen[0]*0.5,screen[1]*0.25,t)
    time.sleep(1)

'''向下滑'''
def swipe_down(dr, t=500, n=1):
    screen = get_size(dr)
    for i in range(n):
        dr.swipe(screen[0]*0.5,screen[1]*0.25,screen[0]*0.5,screen[1]*0.75,t)
    time.sleep(1)


'''向左滑'''
def swipe_left(dr, t=500, n=1):
    screen = get_size(dr)
    for i in range(n):
        dr.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5)
    time.sleep(1)

'''向右滑'''
def swipe_right(dr,t=500,n=1):
    screen = get_size(dr)
    for i in range(n):
        dr.swipe(screen[0]*0.25, screen[1]*0.5, screen[0]*0.75, screen[1]*0.75)
    time.sleep(1)

'''点击坐标位置'''
def zuobiaodanji(dr, a, b, c, d):
    screen = get_size(dr)
    dr.tap([(int(float(a) / float(c) * screen[0]), int(float(b) / float(d) * screen[1]))])


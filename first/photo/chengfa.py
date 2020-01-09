# for i in range(1, 10):
#     print()
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (i, j, i*j), end=' ')

# dicts = {1: 'a', 2: 'b'}
# a = []
# for key, value in dict.items(dicts):
#     a.append(value)
#     print(key, value)
# print(a)
# f1 = 1
# f2 = 1
# for i in range(1, 12):
#     print('%12ld %12ld' % (f1, f2))
#     if (i % 3) == 0:
#         print()
#     f1 = f1 + f2
#     f2 = f1 + f2
# from math import sqrt
# for i in range(2, int(sqrt(120)+1)):
#     if 119 % i == 0:
#         print(i)

# for i in range(100, 1000):
#     j = i // 100
#     k = i // 10 % 10
#     n = i % 10
#     if i == j**3 + k**3 + n**3:
#         print(i)
# n=int(input("输入一个正整数:"))
# print("%d = " % n, end="")
# while n not in [1]:
#     for index in range(2, n+1):
#         if n % index == 0:
#             n = int(n / index)
#             if n==1:
#                 print(index)
#             else:
#                 print("{} * ".format(index), end="")
#             break

# def score_input(score):
#     if score >= 90:
#         print('A')
#     elif score >=60:
#         print('B')
#     else:
#         print('C')
# score_input(99)
# import time
# print(time.time())
# print(time.localtime())
# print(time.asctime())
# print(time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
# import datetime
# print(datetime.date.today())
# print(datetime.date(2019, 11, 3))

# n = 'ajfio29 l1l;ajdf29'
# a = 0
# b = 0
# c = 0
# d = 0
# for i in n:
#     if i.isalpha():
#         a +=1
#     elif i.isspace():
#         b +=1
#     elif i.isdigit():
#         c +=1
#     else:
#         d +=1
# print(a,b,c,d)
from legacy import reduce
# a= 1
# b = []
# for i in range(10):
#     a = a *10
#     b.append(a)
# print(reduce(lambda x,y : x+y, b))
# a= []
# for i in range(2, 1001):
#     for j in range(1, i):
#         if i % j == 0:
#             a.append(j)
#     if i == reduce(lambda x, y : x+y, a):
#         print(i, a)
#     a = []
# a = 1
# for i in range(9, 0, -1):
#     a = (a+1)*2
# print(a)
# def fun(a):
#     # b=0
#     if a == 0:
#         # b=1
#         return 4
#     else:
#         # b=fun(a-1)+a
#         return fun(a-1)+a
# print(fun(0))
# for a in ['x','y','z']:
#     for b in ['x', 'y', 'z']:
#         for c in ['x', 'y', 'z']:
#             if(a!=b)and(b!=c)and(c!=a) and (a!='x') and (c!='x') and (c!='z'):
#                 print ('a和%s比赛，b和%s比赛，c和%s比赛' %(a,b,c))

# for i in range(1, 5):
#     print(' ' * (4 - i), end="")
#     for j in range(1, 2 * i):
#         print('*', end="")
#     print()
# for i in range(3, 0, -1):
#     print(' ' * (4-i), end="")
#     for k in range(1, 2 * i):
#         print('*', end="")
#     print()
# a= 1
# for i in range(1,9):
#     a *= i
#     print(a)
# print(a)
# j = 'abcdefg'
# j = list(j)
# print(j[0:-1])
# j.reverse()
# print(j)
# def fn(s):
#     if len(s)==1:
#         return(s[0])
#     else:
#         a=s[-1]
#         s=s[:-1]
#         return(a+fn(s))
# print(type(fn('123456')))
'''
Saturday
Sunday
Friday
Monday
Tuesday
Thursday
Wednesday
'''
# your_input = input('please input your word:')
# if your_input == 'M':
#     print('Monday')
# elif your_input == 'F':
#     print('Friday')
# elif your_input == 'W':
#     print('Wednesday')
# elif your_input == 'S':
#     print('please input next word:')
#     next_input = input('your input:')
#     if next_input == 'a':
#         print('Saturday')
#     elif next_input == 'u':
#         print('Sunday')
#     else:
#         print('input error1')
# elif your_input == 'T':
#     print('please input next word:')
#     next_input = input('your input:')
#     if next_input == 'u':
#         print('Tuesday')
#     elif next_input == 'h':
#         print('Thursday')
#     else:
#         print('input error2')
# else:
#     print('input error3')
# OKBLUE = '\033[94m'
# BOLD = '\033[1m'
# print(OKBLUE+'DS'+BOLD+'SD')

# lower = int(input("输入区间最小值: "))
# upper = int(input("输入区间最大值: "))

# for num in range(lower,upper + 1):
#     # 素数大于 1
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
# for num in range(10,20):  # 迭代 10 到 20 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          j=num/i          # 计算第二个因子
#          print('循环中%s %s %s'% (i,num,j) )
#          break
#    else:
#        print('循环外%s'% (num))
a = []
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(j)
# print(a)
# def list_num(ln):
#     n = int(input('your insert input:'))
#     for i in range(len(ln)):
#         a = ln[i]
#         b = ln[i+1]
#         if a < n < b:
#             ln.insert(i+1, n)
#     print(ln)
# list_num([1,2,3,4,5,6,8,9,10])
# a = [1,4,6,9,13,16,19,28,40,100,0]
# number = 7
# for i in range(10):
#     if a[i] > number:
#         temp1 = a[i]
#         a[i] = number
#         for j in range(i + 1,11):
#             temp2 = a[j]
#             a[j] = temp1
#             temp1 = temp2
#         break

# a = 5
# for i in range(3):
#     b = 5
#     b+=1
#     a+=1
# print(a,b)
# a = []
# for i in range(101):
#     a.append(i)
# print(reduce(lambda x,y:x+y,a))

# def Fox(number):
#     return number * number
#
# a = True
# while a:
#     input_num = int(input('input:'))
#     if Fox(input_num) >= 50:
#         a = True
#     else:
#         a = False
# import random
# random.uniform
# a = 1000
# # b = a ^ 3
# b = a >> 4
# c = a << 4
# print(a,b,a,c)

from tkinter import *
# canvas = Canvas(width=600, height=400, bg='red')
# canvas.pack(expand=YES, fill=BOTH)
# k=1
# j=1
# for i in range(0,26):
#     canvas.create_oval(310-k, 250-k, 310+k, 250+k, width=2)
#     k +=j
#     j +=0.3
# mainloop()
# top = Tk()
# li = ['c', 'python', 'php', 'html', 'sql', 'java']
# movie = ['css', 'jquery', 'bootstrap']
# listb = Listbox(top)
# listb2 = Listbox(top)
# for item in li:
#     listb.insert(0, item)
# for item in movie:
#     listb2.insert(0, item)
# def helloCall():
#     messagebox.showinfo('hello world','hello python')
# b = Button(top,text='click',bg='red', fg='yellow', command= helloCall)
# b.pack()
# b.flash()
# listb.pack()
# listb2.pack()
# cv = Canvas(top,width=300, height=300, bg='green')
# cv.create_arc(10,50,240,210,start=0, extent=150, fill="blue")
# cv.create_polygon(10,20,30,40,50,60,70,80,fill="blue")
# cv.pack(expand=YES, fill=BOTH)
# x0 = 163
# y0 = 163
# x1 = 175
# y1 = 175
# # cv.create_line(x0,y0,x0,y1, width=1, fill='red')
# for i in range(19):
#     cv.create_line(x0,y0,x0,y1, width=1, fill='red')
#     x0 = x0 - 5
#     y0 = y0 - 5
#     x1 = x1 + 5
#     y1 = y1 + 5
#
# x0 = 163
# y0 = 163
# y1 = 175
# for i in range(21):
#     cv.create_line(x0,y0,x0,y1,fill='red')
#     x0 += 5
#     y0 -=5
#     y1 -=5
#
# x0 = 163
# y0 = 163
# y1 = 175
# for i in range(21):
#     cv.create_line(x0,y0,x0,y1,fill='red')
#     x0 += 5
#     y0 +=5
#     y1 +=5
# top.title('Canvas Titles')
# cv = Canvas(top, width=400, height=400, bg='yellow')
# x0 = 163
# y0 = 163
# x1 = 175
# y1 = 175
# for i in range(19):
#     cv.create_rectangle(x0, y0, x1, y1)
#     x0 -=5
#     y0 -=5
#     x1 +=5
#     y1 +=5
# cv = Canvas(width=300, height=300, bg='green')
# cv.pack(expand=YES, fill=BOTH)
# x0 = 150
# y0 = 100
# cv.create_oval(x0-10, y0-10, x0+10, y0+10)
# cv.create_oval(x0-20, y0-20, x0+20, y0+20)
# cv.create_oval(x0-50, y0-50, x0+50, y0+50)
# import math
# B = 0.809
# for i in range(16):
#     a = 2 * math.pi / 16 * i
#     x = math.ceil(x0 + 48 * math.cos(a))
#     y = math.ceil(y0 + 48 * math.sin(a) * B)
#     cv.create_line(x0, y0, x, y, fill='red')
# cv.create_oval(x0-60, y0-60, x0+60, y0+60)
# for k in range(501):
#     for i in range(17):
#         a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
#         x = math.ceil(x0 + 48 * math.cos(a))
#         y = math.ceil(y0 + 48 + math.sin(a) * B)
#         cv.create_line(x0, y0, x, y, fill = 'red')
#     for j in range(51):
#         a = (2 * math.pi / 16) * j + (2 * math.pi / 180) * k -1
#         x = math.ceil(x0 + 48 * math.cos(a))
#         y = math.ceil(y0 + 48 + math.sin(a) * B)
#         cv.create_line(x0, y0, x, y, fill = 'red')
# mainloop()
# a = []
# for i in range(10):
#     a.append([])
#     for j in range(10):
#         a[i].append(0)
# for i in range(10):
#     a[i][0] = 1
#     a[i][i] = 1
# for i in range(2, 10):
#     for j in range(1, i):
#         a[i][j] = a[i-1][j-1] + a[i-1][j]
# print(a)
# for i in range(2):
#     print('i:',i)
#     for j in range(10):
#         print('j:',j)
#         for k in range(5):
#             print(k)
# x = 360
# y = 160
# top = 130
# bottom = 130
# cv = Canvas(width=500, height=600, bg='white')
# for i in range(20):
#     cv.create_oval(250-top, 250-bottom, 250+top, 250+bottom)
#     top -=5
#     bottom +=5
# cv.pack()
# mainloop()
# cv = Canvas(width=400, height=600, bg='white')
# left = 20
# right = 50
# top = 50
# num = 15
# for i in range(num):
#     cv.create_oval(250-right, 250 -left, 250+right, 250+left)
#     cv.create_oval(250-20, 250-top, 250+20, 250+top)
#     cv.create_rectangle(20-2*i, 20-2*i, 10*(i+2), 10*(i+2))
#     right +=5
#     left +=5
#     top +=10
# cv.pack()
# mainloop()

# import math
# class PTS:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
# points = []
# def LineDemo():
#     screeenx = 500
#     screeeny = 500
#     cv = Canvas(width=screeenx, height=screeeny, bg='white')
#     Aspect = 0.85
#     Maxpts = 15
#     h = screeeny
#     w = screeenx
#     xcenter = w / 2
#     ycenter = h / 2
#     radius = (h - 20) / (Aspect * 2) - 20
#     step = 360 / Maxpts
#     angle = 0.0
#     for i in range(Maxpts):
#         rads = angle = math.pi / 180.0
#         p = PTS()
#         p.x = xcenter + int(math.cos(rads) * radius)
#         p.y = ycenter - int(math.sin(rads) * radius * Aspect)
#         angle += step
#         points.append(p)
#     cv.create_oval(xcenter - radius, ycenter - radius, xcenter + radius, ycenter + radius)
#     print(points)
#     for i in range(Maxpts):
#         for j in range(i, Maxpts):
#             cv.create_line(points[i].x, points[i].y, points[j].x, points[j].y)
#     cv.pack()
#     mainloop()
# LineDemo()

# for i in range(5):
#     n = 0
#     if i != 1: n += 1
#     if i == 3: n += 1
#     if i == 4: n += 1
#     if i != 4: n += 1
#     print(n)

# person = {"li":18,"wang":15,"zhang":60,"sun":77}
# m = 'li'
# for key in person.keys():
#     if person[m] < person[key]:
#         m = key
#         print(m)
# print ('%s,%d' % (m,person[m]))
#
# str1 = 'sdkf'
# str2 = 'acb'
# list1 = []
# list1.extend([str1,str2])
# list1.sort()
# print(list1)
# for item in list1:
#     print(item)

# i = 0
# j = 1
# x = 0
# while(i<5):
#     x = 4 * j
#     for i in range(0, 5):
#         if(x%4 != 0):
#             break
#         else:
#             i +=1
#         x = (x/4) * 5 +1
#     j +=1
# print(x)

# a = 809
# for i in range(2, 13):
#     b = i * a
#     if b >=1000 and b <= 10000 and 8 * i < 100 and 9 * i >=100:
#         print(b,i)
# a = '122'
# n = 0
# for i in range(len(a)):
#     n = n * 8 + ord(a[i]) - ord('0')
# print(n)

# sum = 4
# n = 4
# for i in range(2,9):
#     if i <=2:
#         n *=7
#     else:
#         n *=8
#     sum +=n
#
# delimiter = '|'
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))
# i = 1
# j = 1
# n = 9
# sum = 9
# num = int(input('input:'))
# while i !=0:
#     if n % num == 0:
#         i = 0
#     else:
#         sum *= 10
#         n += sum
#         j += 1
# print(n,j)

# n = 1
# while n <= 7:
#     a=int(input('your input:\n'))
#     while a < 1 or a > 50:
#         a = int(input('your input2:\n'))
#     print(a * '*')
#     n += 1
#
num = int(input('your four input:'))
aa = []
aa.append(num // 1000)
aa.append(num % 1000 // 100)
aa.append(num % 100 // 10)
aa.append(num % 10)
for i in range(4):
    aa[i] += 5
    aa[i] %= 10
for i in range(2):
    aa[i], aa[3 - i] = aa[3 - i], aa[i]
l = [str(i) for i in aa]
m = int(''.join(l))
print(m)
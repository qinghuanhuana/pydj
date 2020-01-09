#coding=utf-8
import time


def add(n, i):
      return n+i

def test():
      for i in range(4):
          yield i
          # return i
g = test()
for f in  [1,2,3,10,111]:
    g =  (add(2, i)  for i in g)
print(list(g))  # 结果是 [15, 16, 17, 18]

#coding=utf-8
import time


def add(n, i):
      return n+i

def test():
      for i in range(4):
            yield i
g = test()
for n in  [1,  10,  5]:
    g =  (add(n, i)  for i in g)
print(list(g))  # 结果是 [15, 16, 17, 18]

# coidng=utf-8

a = [1, 5, 2, 2, 1, 3, 3, 2, 1, 3, 4, 2, 5, 4]
quchong = set(a)
print (quchong)
d = {}
for i in quchong:
    d[i] = a.count(i)
print(d)
print(d.items())
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)
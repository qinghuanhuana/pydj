import os
dirpath = os.path.dirname(os.path.abspath('__file__'))
print(dirpath)
a = 0
for root, dirs, names in os.walk(dirpath):
    print(root,dirs,names)
    for name in names:
        if os.path.splitext(name)[1] == '.py':
            a +=1
# print(a)

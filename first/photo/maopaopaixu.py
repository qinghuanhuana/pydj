a = [3, 2, 1, 4, 5, 6, 7]
for i in range(0, len(a)-1):
    flag = True
    for j in range(0, len(a)-1-i):
        if a[j] > a[j+1]:
            flag = False
            a[j], a[j+1] = a[j+1], a[j]
    print(flag)
    if flag:
        break
print(a)
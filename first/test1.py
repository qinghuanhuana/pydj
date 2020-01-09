a = [0,1,2,3,4,5,6,7,8,9]
generator_ex = (x*x for x in range(10))

for i in range(2):
    i = generator_ex
print(list(i))



import time
import random

while True:
    i = random.randint(0, 2**32) % 100
    print ('input you guess:\n')
    start = time.clock()
    b = time.time()
    guess = int(input('input your guess:\n'))
    while guess != i:
        if guess > i:
            print('smaller')
            guess = int(input('input your guess:\n'))
        elif guess == i:
            break
        else:
            print('bigger')
            guess = int(input('input your guess:\n'))

    end = time.clock()
    d = time.time()
    var = (end - start) / 18.2
    print(var)

    if var < 15:
        print('clever')
    elif var < 25:
        print('normal')
    else:
        print('stupid')
    print('congresdultions')
    print('number you gues is %d' % i)

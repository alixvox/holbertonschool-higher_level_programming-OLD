#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = abs(number)
last_dig = abs_num % 10
print("Last digit of {:d} is {:d} ".format(number, last_dig), end='')
if last_dig < 6 and last_dig != 0:
    print("and is less than 6 and not 0")
elif last_dig > 5:
    print("and is greater than 5")
else:
    print("and is 0")

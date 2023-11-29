#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
m = int(n[:2])
p = int(n[-1])
if p > 5 and m > -1:
    print(f"Last digit of {n} is {p} and is greater than 5")
elif p == 0 and m > -1:
    print(f"Last digit of {n} is {p} and is 0")
elif m < 0 and p != 0:
    print(f"Last digit of {n} is -{p} and is less than 6 and not 0")
elif m < 0 and p == 0:
    print(f"Last digit of {n} is {p} and is 0")
else:
    print(f"Last digit of {n} is {p} and is less than 6 and not 0")

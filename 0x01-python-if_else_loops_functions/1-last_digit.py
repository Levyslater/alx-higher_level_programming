#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
if int(n[-1]) > 5 and int(n[0]) > -1:
    print(f"Last digit of {n} is {n[-1]} and is greater than 5")
elif int(n[-1]) == 0 and int(n[0] > -1:
    print(f"Last digit of {n} is {n[-1]} and is 0")
elif int(n[0]) < 0:
    print(f"Last digit of {n} is -{n[-1]} and is less than 6 and not 0")
else:
    print(f"Last digit of {n} is {n[-1]} and is less than 6 and not 0")

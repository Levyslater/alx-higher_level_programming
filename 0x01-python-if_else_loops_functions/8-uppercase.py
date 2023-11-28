#!/usr/bin/python3
def islower(i):
    if ord(i) >= 97 and ord(i) <= 122:
        return True
    else:
        return False


def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i) if not islower(i) else ord(i) - 32), end='')
    print('')

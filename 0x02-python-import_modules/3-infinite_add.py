#!/usr/bin/python3

if __name__ == "__main__":
    """add and print arguments"""
    import sys
    m = 0
    ac = len(sys.argv) - 1

    for i in range(ac):
        m += int(sys.argv[i + 1])
    print(m)

import math

num = int(input("Please enter a number: "))

if num == 2:
    print(f"{num} is prime")
elif num == 1:
    print("1 is not prime")
elif num <= 0:
    raise ValueError("number must be greater than 0")
else:
    root  = math.ceil(math.sqrt(num))

    for val in range(2, root + 1):
        if num % val == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
from math import factorial

num = int(input())

while num != 0:
    result = int((factorial(num))/6)
    print(result)
    new = int(input())
    num = new

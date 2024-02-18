from functools import reduce

def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mmc(a, b):
  
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // euclides(a, b)

values = map(int, input().split())

print(reduce(mmc,values))
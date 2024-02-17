from functools import reduce
import math

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

numbers = map(int, input().split())
mmc = reduce(lcm, numbers)
print(mmc)
    



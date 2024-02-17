from functools import reduce
from math import gcd

values = map(int, input().split())

res = reduce(gcd, values)
print(res)
    
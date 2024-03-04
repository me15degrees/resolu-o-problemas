from math import lcm
from functools import reduce

nums = [int(input()) for _ in range(3)]

print(reduce(lcm,nums))

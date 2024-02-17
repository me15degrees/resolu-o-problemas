from math import gcd

c, l = map(int, input().split())

res = c * l // gcd(c,l) ** 2

print(res)


from math import factorial

influencer = int(input())

result = factorial(influencer) / (2 * factorial (influencer - 2))

print(int(result))




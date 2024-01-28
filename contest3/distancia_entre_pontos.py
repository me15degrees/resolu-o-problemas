from math import sqrt
ponto_a = (int(input()),int(input()))
ponto_b = (int(input()),int(input()))

def distance(a,b):
    d = sqrt(((ponto_a[0]-ponto_b[0])**2 + (ponto_a[1]-ponto_b[1])**2))
    return d

print(distance(ponto_a,ponto_b))
from math import sqrt
a = 1
b = 1
c = 4
delta = b**2*(-4 * a * c)
x = -b + sqrt(delta) / (2*a)

if delta < 0:
    print("nao existem raizes reais")

elif delta == 0:
    print(f"existe 1 raiz real: {x}")
elif delta > 0: 
    x_ = -b - sqrt(delta) / (2*a)
    print(f"existem 2 raizes reais: {x} e {x_}")
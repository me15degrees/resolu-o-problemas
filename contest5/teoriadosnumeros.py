def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)

def solve_diophantine(a, b, c):
    gcd, x0, y0 = extended_gcd(a, b)
    
    if c % gcd != 0:
        return "Não tem solução inteira."
    
    else:
        # Encontrar uma solução particular
        x0 *= c // gcd
        y0 *= c // gcd
        return (x0, y0)

# Exemplo de uso
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

solution = solve_diophantine(a, b, c)
print("Solução para a equação {}x + {}y = {}: x = {}, y = {}".format(a, b, c, solution[0], solution[1]))


# encontre o mdc dos coeficientes usando o algoritmo de euclides
# escreva o mdc(a,b) = c como combinação linear dos coeficientes 252 e 105
# multiplique o mdc(a,b) = c de modo a obter o termo independente 42

from math import gcd

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

def euler_theorem(a, n):
    if gcd(a, n) != 1:
        return None  # a e n não são coprimos
    return pow(a, phi(n), n)

# Exemplo de uso:
a = 7
n = 15
result = euler_theorem(a, n)
print(f"{a}^{phi(n)} mod {n} = {result}")

from math import gcd

def decimals_to_fraction(num):

    numero_str = str(num)

    if '.' in numero_str:
        indice_ponto = numero_str.index('.')
        zeros = len(numero_str) - indice_ponto - 1
        base = 10**zeros

    numerador, denominador = int((num*base))//gcd(int(num*base),base), base//gcd(int(num*base),base)
    
    return f"{numerador}/{denominador}"

print(decimals_to_fraction(0.60))
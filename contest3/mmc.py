def euclides(a, b):
    while b != 0:
        a, b = b, a % b
        print(f"este é o a: {a}, este é o b: {b}")
    return a

a = 48
b = 18

mdc = euclides(a, b)

def mmc(a, b):
    # Verifica se a e b são diferentes de zero para evitar divisão por zero
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // euclides(a, b)

# Exemplo de uso
a = 12
b = 18

mmc_resultado = mmc(a, b)
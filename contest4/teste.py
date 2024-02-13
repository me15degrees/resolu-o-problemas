from itertools import permutations
from functools import reduce
from math import factorial
from unicodedata import normalize

def combinatoria():
    camisetas = 6
    calcas = 4
    sapatos = 2

    resultado = camisetas * calcas * sapatos

    print(f"o resultado da combinação é: {resultado}")
    return resultado


def remove_accents(word: str) -> str:
    return normalize("NFKD", word).encode("ASCII", "ignore").decode("ASCII")

def permutacoes_com_repeticao(palavra):
    numerador = factorial(len(palavra))
    denominador = []
    letras = set(palavra)
    for i in letras:
        if palavra.count(i) > 1:
            denominador.append(factorial(palavra.count(i)))
    
    return numerador / reduce(lambda x, y: x * y, denominador)


palavra = "programação"
resultado = permutacoes_com_repeticao(remove_accents(palavra))
print(resultado)
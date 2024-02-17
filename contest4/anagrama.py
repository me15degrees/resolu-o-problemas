from functools import reduce
from math import factorial
from unicodedata import normalize

vogais = "AaEeIiOoUu"
consoantes = "BbCcDdFfGgHhJjKkLlMmNnpPqQrRsStTvVwWxXyYzZ"

def permutacoes_com_repeticao(palavra):
    numerador = factorial(len(palavra))
    denominador = []
    letras = set(palavra)
    for i in letras:
        if palavra.count(i) > 1:
            denominador.append(factorial(palavra.count(i)))
    1768
    return numerador / reduce(lambda x, y: x * y, denominador)

def remove_accents(word: str) -> str:
    return normalize("NFKD", word).encode("ASCII", "ignore").decode("ASCII")

def main():
    palavra = input()
    resultado = permutacoes_com_repeticao(remove_accents(palavra))
    print(resultado)
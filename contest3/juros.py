"""Capital de R$500 valoriza a juros simples de 3% ao mês. Ou seja R$15
por mês. Depois de um ano foi acumulado R$180 de juros (15x12).

Na fórmula:
J = C . I . T -> J = 500 . 3/100 . 12 = 180"""

capital = 500
juros = 0.03
tempo = 12

juros = capital * juros * tempo
print(juros)

"""
A diferença dos juros compostos para o simples é que o simples sempre é calculado sobre o valor do capital inicial, 
já o composto é calculado sobre o valor do exercício anterior, ou seja no segundo mês é
calculado sobre o valor acumulado no primeiro mês. A fórmula é M = C(1 + i)^t onde M é valor final da transação.

Exemplo:
Capital de R$500 valoriza a juros compostos de 3% ao mês. Quanto dinheiro é acumulado em 12 meses?"""


capital = 500
juros = 0.03
tempo = 12
montante = capital *(1+juros)**tempo

print(montante)


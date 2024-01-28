list1 = [10, 2, 4, 5, 1, 9, 40, 6, 7, 8, 3]

for i in range(1, len(list1)):
    key = list1[i] # como não há números a esquerda do i, ele começa sendo o valor mínimo
    j = i - 1 # j será o antecessor de i

    # só entra no while depois do i ser 1 e o j ser 0
    while j >= 0 and key < list1[j]:
        list1[j + 1] = list1[j] # move os elementos maiores que key para uma posição a frente
        j -= 1
    list1[j + 1] = key # insere key na posição correta

print(list1)

# não tinha conseguido andar com os números maiores que a variável key
"""
nº de comparações - n(n-1)/2
nº de trocas - n(n-1)/2
"""
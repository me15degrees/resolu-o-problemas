lista = [item for item in range(13,4,-1)]
pesos = [_ for _ in range(0,9)]
size = len(lista)

def media_simples(lista):
    media = sum(lista)/len(lista)

    return media

def media_ponderada(lista,pesos,size):
    soma = 0
    for i in range(size):
        multiply = lista[i]*pesos[i]
        soma += multiply
    soma_pesos = sum(pesos)
    return soma/soma_pesos
        
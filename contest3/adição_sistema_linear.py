matriz1 = [0, 1, 2, 4]
matriz2 = [1, 2, 1, 1, 1]

size1 = len(matriz1)
size2 = len(matriz2)
dif = abs(size1-size2)

if size1 > size2:
    for i in range(dif):
        matriz2.append(0)
elif size1 < size2:
    for i in range(dif):
        matriz1.append(0)


for i in range(len(matriz1)):
    matriz1[i] = matriz1[i] + matriz2[i]

print(matriz1)


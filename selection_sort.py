list1 = [0, 2, 4, 5, 1, 9, 40, 6, 7, 8, 3]

for i in range(len(list1)):  # n
    min_index = i
    for j in range(i + 1, len(list1)):  # n*n
        if list1[j] < list1[min_index]:
            min_index = j
            
    
    list1[i], list1[min_index] = list1[min_index], list1[i]

print(list1)

# tinha errado o min_index, porque não igualei a i, mas a 0
# guardava o valor em uma variável min, e não o seu index

"""
nº de comparações - n(n-1)/2
nº de trocas - n
"""
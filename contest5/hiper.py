def eh_primo(num):
    if num < 2: 
        return 0
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return 0
    return 1

n = int(input())

for i in range(n):
    num = int(input())  
    print(eh_primo(num))

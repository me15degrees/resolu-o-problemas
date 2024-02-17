x, y = map(int, input().split())

def eh_primo(num):
    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True

soma = 0

for i in range(x ,y + 1):
    if eh_primo(i):
        soma += i

print(soma)
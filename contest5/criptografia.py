def eh_primo(num):
    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True

num = int(input())

possivel = 0
for i in range(2, num):
    if eh_primo(i) and eh_primo(num // i): 
        possivel = 1
        break 

print(possivel)

def eh_primo(num):
    if num < 2: 
        return False
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False
    return True

for m in range(int(input())):
    num = int(input())

    possivel = 0
    for i in range(2, num):
        for j in range(2,num):
            if eh_primo(i) and eh_primo(j) and i + j == num:
                possivel = 1
                break   

    print(possivel)


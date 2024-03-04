num = int(input())

for _ in range(num):
    word = input()
    word = word.replace("a","@").replace("e","&").replace("i","!").replace("o","*").replace("u","%")
    print(word)
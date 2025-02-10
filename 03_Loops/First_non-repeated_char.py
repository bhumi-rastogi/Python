n = int(input())
for char in n:
    if n.count(char) == 1:
        print(char)
        break
    
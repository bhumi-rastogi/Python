n = int(input())
for i in range(1,11):
    if i == 5:
        continue
    print(f"{n} * {i} = {n*i}")
password = input()
length = len(password)

if length < 6:
    print("Weak")
elif length <=10 :
    print("Medium")
else:
    print("Strong")
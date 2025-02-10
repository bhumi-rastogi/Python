age = int(input("Give me an age: "))
day = input("Give me a day: ")
price = 12 if age >= 18 else 8
price -=2 if day=="Wednesday" else price
print("Price of ticket is $",price)


# if age < 18:
#     price = 8
# else:
#     price = 12

# if day == "Wednesday":
#     price-=2

# print(f"${price}")
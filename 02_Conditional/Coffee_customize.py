order_size = input()
extra_shot = input()

if extra_shot:
    coffee = order_size + " extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)
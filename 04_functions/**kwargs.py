def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Bhumi",power="cute")
print_kwargs(name="Bhumi")
print_kwargs(name="Bhumi",power="cute",age=19)
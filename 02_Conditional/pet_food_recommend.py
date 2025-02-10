pet = input()
age = int(input())

if pet == 'dog':
    if age < 2:
        food = 'Puppy food'
    else:
        food = 'Dog food'
elif pet == 'cat':
    if age < 5:
        food = 'Kitten food'
    else:
        food = 'Cat food'
else:
    print("Not enough information.")
score = int(input("Give me an input: "))

if score>=101:
    print("Verify your grade again")
    exit()
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade ="F"
print(grade)
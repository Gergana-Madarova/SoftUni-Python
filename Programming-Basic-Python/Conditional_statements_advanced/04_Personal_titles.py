age = float(input())
gender = input()

if age >= 16 and gender == 'f':
    print("Ms.")
elif age >= 16 and gender == 'm':
    print("Mr.")
elif age < 16 and gender == 'f':
    print("Miss")
elif age < 16 and gender == 'm':
    print("Master")
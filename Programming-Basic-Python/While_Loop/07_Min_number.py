import sys

number = input()
min = sys.maxsize

while number != "Stop":
    number = int(number)
    if number < min:
        min = number

    number = input()

print(min)
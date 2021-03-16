import sys

number = input()
max = -sys.maxsize - 1

while number != "Stop":
    number = int(number)
    if number > max:
        max = number

    number = input()

print(max)
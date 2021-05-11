numLines = int(input())
sum = 0

for i in range(1, numLines + 1):
    letter = ord(input())
    sum += letter

print(f"The sum equals: {sum}")

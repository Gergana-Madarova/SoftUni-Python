sequence = input()
sum = 0

for ch in sequence:
    if ch == 'a':
        sum +=1
    elif ch == 'e':
        sum +=2
    elif ch == 'i':
        sum += 3
    elif ch == 'o':
        sum += 4
    elif ch == 'u':
        sum +=5

print(sum)
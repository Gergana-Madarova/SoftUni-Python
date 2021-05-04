divisor = int(input())
bound = int(input())

num = bound

for i in range(bound, divisor + 1, -1):
    if(num % divisor == 0):
        num = i
        break
    num -= 1

print(num)

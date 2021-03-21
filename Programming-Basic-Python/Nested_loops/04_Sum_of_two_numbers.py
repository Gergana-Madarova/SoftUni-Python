start = int(input())
end = int(input())
number = int(input())

count = 0
is_find = False

for i in range (start, end + 1):
    for j in range (start, end + 1):
        count +=1
        if i + j == number:
            print(f"Combination N:{count} ({i} + {j} = {number})")
            is_find = True
            break

    if(is_find == True):
        break

if(is_find == False):
    print(f"{count} combinations - neither equals {number}")
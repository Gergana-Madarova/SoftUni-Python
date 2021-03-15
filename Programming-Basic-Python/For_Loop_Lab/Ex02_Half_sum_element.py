import sys

n = int(input())
max_num = -sys.maxsize
sum_nembers = 0

for i in range(0, n):
    num = int(input())
    sum_nembers += num

    if num > max_num:
        max_num = num

if max_num == sum_nembers - max_num:
    print("Yes")
    print(f"Sum = {sum_nembers - max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (sum_nembers - max_num))}")
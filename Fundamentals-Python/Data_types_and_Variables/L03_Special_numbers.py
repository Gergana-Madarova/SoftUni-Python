n = int(input())

for i in range(1, n+1):
    sum_elements = 0
    special = False
    current_num = i

    while current_num != 0:
        sum_elements += current_num % 10
        current_num = current_num // 10

    if sum_elements == 5 or sum_elements == 7 or sum_elements == 11:
        special = True

    print(f"{i} -> {special}")

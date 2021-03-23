min_num = int(input())
max_num = int(input())

for number in range (min_num, max_num + 1):
    odd_sum = 0
    even_sum = 0
    number_to_string = str(number)

    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            odd_sum += int(digit)   #започваме от 0-ев индекс, който е 1-ва позиция т.е. нечетна
        else:
            even_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')
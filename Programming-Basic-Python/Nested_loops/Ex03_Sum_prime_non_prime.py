num = input()
sum_prime = 0
sum_non_prime = 0

while num.lower() != "stop":
    current_num = int(num)

    if current_num < 0:
        print("Number is negative.")
    elif current_num % 2 == 0:
        if current_num == 2:
            sum_prime += current_num
        else:
            sum_non_prime += current_num
    elif current_num == 3 or current_num == 5:
        sum_prime += current_num
    elif current_num % 2 != 0 and current_num % 3 != 0 and current_num % 5 != 0:
        sum_prime += current_num
    else:
        sum_non_prime += current_num

    num = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
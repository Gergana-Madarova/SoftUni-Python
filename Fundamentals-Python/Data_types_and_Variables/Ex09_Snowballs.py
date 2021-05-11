from math import pow

number_of_snowballs = int(input())
output = ""
current_snowball_value = 0.0

for i in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = pow((snowball_snow / snowball_time), snowball_quality)
    #snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > current_snowball_value:
        current_snowball_value = snowball_value
        output = f"{snowball_snow} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"

print(output)

n = int(input())
liters_in_tank = 255

for i in range(1, n + 1):
    quantities = int(input())

    if liters_in_tank - quantities < 0:
        print("Insufficient capacity!")
    else:
        liters_in_tank -= quantities

print(255 - liters_in_tank)

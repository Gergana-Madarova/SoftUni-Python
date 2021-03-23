counterFloor = int(input())
counterRoom = int(input())

for i in range (counterFloor, 0, -1):
    if counterFloor == i:
        for j in range (0, counterRoom):
            print(f"L{i}{j}", end=" ")
        print()
    elif (i % 2 == 1):
        for j in range (0, counterRoom):
            print(f"A{i}{j}", end=" ")
        print()
    else:
        for j in range (0, counterRoom):
            print(f"O{i}{j}", end=" ")
        print()
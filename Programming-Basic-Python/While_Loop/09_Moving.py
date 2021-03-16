width = int(input())
lenght = int(input())
hight = int(input())

free_space = width * lenght * hight
count_box = input()
is_free = True

while count_box != "Done":
    count_box = int(count_box)
    free_space -= count_box

    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        is_free = False
        break

    count_box = input()

if is_free:
    print(f"{free_space} Cubic meters left.")
desire_book = input()
count = 0
book = input()
is_found = False

while book != "No More Books":
    count +=1
    if book == desire_book:
        print(f"You checked {count - 1} books and found it.")
        is_found = True
        break

    book = input()

if is_found == False:
    print("The book you search is not here!")
    print(f"You checked {count} books.")
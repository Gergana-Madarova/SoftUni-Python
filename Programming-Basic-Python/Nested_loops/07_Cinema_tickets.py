film = input()
all_tickets = 0
counter_tickets = 0
counter_student = 0
counter_standard = 0
counter_kid = 0

while film != "Finish":
    free_seat = int(input())
    for i in range (1, free_seat + 1):
        type_of_ticket = input()
        if type_of_ticket != "End":
            counter_tickets += 1
            if type_of_ticket == "student":
                counter_student += 1
            elif type_of_ticket == "standard":
                counter_standard += 1
            elif type_of_ticket == "kid":
                counter_kid += 1
        else:
            break

    tickets_percent = counter_tickets * 100 / free_seat
    all_tickets += counter_tickets
    counter_tickets = 0

    print(f"{film} - {tickets_percent:.2f}% full.")
    film = input()

student_percent = counter_student * 100 / all_tickets
standard_percent = counter_standard * 100 / all_tickets
kid_percent = counter_kid * 100 / all_tickets
print(f"Total tickets: {all_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
unsatisfactory_grades = int(input())
task = input()
average_score = 0
count = 0
is_unsatisfactory = False
count_task = 0

while task != "Enough":
    last_task = task
    grade = int(input())
    count_task += 1
    average_score += grade

    if grade <= 4:
        count +=1

    if count == unsatisfactory_grades:
        is_unsatisfactory = True
        print(f"You need a break, {unsatisfactory_grades} poor grades.")
        break

    task = input()

if is_unsatisfactory == False:
    print(f"Average score: {average_score/count_task:.2f}")
    print(f"Number of problems: {count_task}")
    print(f"Last problem: {last_task}")
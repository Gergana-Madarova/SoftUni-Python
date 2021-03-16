name = input()

count = 0;
average_grade = 0
is_excluded = False

for i in range (1, 13):
    grade = float(input())
    if grade < 4:
        count +=1
    elif grade >= 4 and grade <= 6:
        average_grade += grade

    if count > 1:
        print(f"{name} has been excluded at {i-1} grade")
        is_excluded = True
        break

if is_excluded == False:
    print(f"{name} graduated. Average grade: {average_grade/12:.2f}")
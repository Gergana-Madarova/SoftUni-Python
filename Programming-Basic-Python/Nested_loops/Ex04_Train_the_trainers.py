numPeople = int(input())

sumGrades = 0
counterPr = 0
averageGr = 0
totalAverageGr = 0

name = input()

while name != "Finish":
    counterPr +=1
    for i in range(1, numPeople +1):
        grade = float(input())
        sumGrades += grade

    averageGr = sumGrades / numPeople
    totalAverageGr += averageGr

    print(f"{name} - {averageGr:.2f}.")
    sumGrades = averageGr = 0

    name = input()

print(f"Student's final assessment is {(totalAverageGr/counterPr):.2f}.")
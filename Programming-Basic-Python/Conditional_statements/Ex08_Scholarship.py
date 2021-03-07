import math

income = float(input())
success = float(input())
min_salary = float(input())

if success >= 5.5:
    if (income > min_salary or (income <= min_salary and 25 * success >= 0.35 * min_salary)):
        scholarship = math.floor(25 * success)
        print(f"You get a scholarship for excellent results {scholarship} BGN")
    elif (income <= min_salary and 25 * success < 0.35 * min_salary):
        scholarship = math.floor(0.35 * min_salary)
        print(f"You get a Social scholarship {scholarship} BGN")
elif success >= 4.5 and income <= min_salary:
    scholarship = math.floor(0.35 * min_salary)
    print(f"You get a Social scholarship {scholarship} BGN")
else:
    print("You cannot get a scholarship!")
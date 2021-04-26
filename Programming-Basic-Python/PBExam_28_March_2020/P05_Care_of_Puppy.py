buyFood = int(input())
eatenFoodGr = input()

totalEatenFood = 0

buyFood = buyFood * 1000

while eatenFoodGr != "Adopted":
    totalEatenFood += int(eatenFoodGr)
    eatenFoodGr = input()

if buyFood >= totalEatenFood:
    print(f"Food is enough! Leftovers: {buyFood-totalEatenFood} grams.")
elif totalEatenFood > buyFood:
    print(f"Food is not enough. You need {totalEatenFood-buyFood} grams more.")

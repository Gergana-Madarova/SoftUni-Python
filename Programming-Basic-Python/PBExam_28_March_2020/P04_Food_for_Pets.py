days = int(input())
totalFood = float(input())

totalFoodDog = 0
totalFoodCat = 0
biscuits = 0.0

for i in range(1, days + 1):
    dogFood = int(input())
    catFood = int(input())

    totalFoodDog += dogFood
    totalFoodCat += catFood

    if i % 3 == 0:
        biscuits = biscuits + 0.1 * (dogFood + catFood)


totalEatenFood = totalFoodDog + totalFoodCat
totalEatenfoodPercent = 100 * (totalEatenFood / totalFood)
totalFoodDogPercent = 100 * (1.0*totalFoodDog / totalEatenFood)
totalFoodCatPercent = 100 * (1.0*totalFoodCat / totalEatenFood)

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{totalEatenfoodPercent:.2f}% of the food has been eaten.")
print(f"{totalFoodDogPercent:.2f}% eaten from the dog.")
print(f"{totalFoodCatPercent:.2f}% eaten from the cat.")

min = int(input())
countWalking = int(input())
calories = int(input())

totalCaloriesForWolking = countWalking * 5 * min
halfCalories = calories / 2

if totalCaloriesForWolking >= halfCalories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {totalCaloriesForWolking}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {totalCaloriesForWolking}.")

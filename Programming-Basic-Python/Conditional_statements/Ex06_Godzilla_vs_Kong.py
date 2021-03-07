movie_budget = float(input())
count_of_extras = int(input())
price_for_clothing_one = float(input())

decor = 0.1 * movie_budget
price_for_clothing_all = count_of_extras * price_for_clothing_one

if (count_of_extras > 150):
    price_for_clothing_all = price_for_clothing_all - (0.1 * price_for_clothing_all)

if (decor + price_for_clothing_all > movie_budget):
    print("Not enough money!")
    print(f"Wingard needs {(decor + price_for_clothing_all - movie_budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(movie_budget - (decor + price_for_clothing_all)):.2f} leva left.")
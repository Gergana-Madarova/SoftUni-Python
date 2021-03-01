price_of_strawberrys = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

price_of_raspberries = price_of_strawberrys / 2
price_of_oranges = price_of_raspberries - (0.4 * price_of_raspberries)
price_of_bananas = price_of_raspberries - (0.8 * price_of_raspberries)

needed_money = strawberry_kg * price_of_strawberrys + raspberries_kg * price_of_raspberries + oranges_kg * price_of_oranges + bananas_kg * price_of_bananas

print(needed_money)
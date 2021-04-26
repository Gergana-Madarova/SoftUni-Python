fruit = input()
size = input()
numOfSets = int(input())

price = 0.0

if size == "big":
    if fruit == "Watermelon":
        price = 5 * 28.70
    elif fruit == "Mango":
        price = 5 * 19.60
    elif fruit == "Pineapple":
        price = 5 * 24.80
    elif fruit == "Raspberry":
        price = 5 * 15.20
elif size == "small":
    if fruit == "Watermelon":
        price = 2 * 56
    elif fruit == "Mango":
        price = 2 * 36.66
    elif fruit == "Pineapple":
        price = 2 * 42.10
    elif fruit == "Raspberry":
        price = 2 * 20

price = price * numOfSets

if price > 1000:
    price = price - (0.5 * price)
elif price >= 400:
    price = price - (0.15 * price)

print(f"{price:.2f} lv.")

degree = int(input())
part_of_day = input()

outfit = ""
shoes = ""

if part_of_day == "Morning" and 10 <= degree <= 18:
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif part_of_day == "Morning" and degree >= 25:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif part_of_day == "Afternoon" and 18 < degree <= 24:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif part_of_day == "Afternoon" and degree >= 25:
    outfit = "Swim Suit"
    shoes = "Barefoot"
else:
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
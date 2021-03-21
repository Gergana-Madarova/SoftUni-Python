destination = input()

while(destination != "End"):
    min_budget = float(input())
    money = 0

    while(min_budget > money):
        money += float(input())

    print(f"Going to {destination}!")
    destination = input()
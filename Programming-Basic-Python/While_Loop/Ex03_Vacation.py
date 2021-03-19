needed_money = float(input())
money_on_hand = float(input())

count = 0
days = 0
is_collect = True

while money_on_hand < needed_money:
    action = input()
    money = float(input())
    days += 1

    if action == "spend":
        if money_on_hand < money:
            money_on_hand = 0
        else:
            money_on_hand -= money
        count += 1
    elif action == "save":
        money_on_hand += money
        count = 0

    if count == 5:
        print("You can't save the money.")
        print(days)
        is_collect = False
        break

if is_collect:
    print(f"You saved the money for {days} days.")
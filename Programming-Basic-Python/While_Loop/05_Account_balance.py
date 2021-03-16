money = input()
balance = 0

while money != "NoMoreMoney":
    money = float(money)
    if money < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {money:.2f}")
    balance += money
    money = input()

print(f"Total: {balance:.2f}")

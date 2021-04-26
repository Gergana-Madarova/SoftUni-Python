pens = int(input())
marckers = int(input())
abstergent = float(input())
percent = int(input())

needMoney = pens * 5.80 + marckers * 7.20 + abstergent * 1.2
needMoney = needMoney - (percent * needMoney / 100)

print(f"{needMoney:.3f}")

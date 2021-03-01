rent = int(input())

price_of_cake = rent * 0.2
price_of_drinks = price_of_cake - 0.45 * price_of_cake
animators = rent / 3
budget = rent + price_of_cake + price_of_drinks + animators

print(budget)
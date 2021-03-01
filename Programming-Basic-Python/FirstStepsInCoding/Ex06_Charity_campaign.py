count_days = int(input())
count_confectioner = int(input())
count_cakes = int(input())
count_gofr = int(input())
count_pancakes = int(input())

cost_cake = 45;
cost_gofr = 5.8;
cost_pancakes = 3.2;

money_per_day = count_confectioner * (count_cakes * cost_cake + count_gofr * cost_gofr + count_pancakes * cost_pancakes)
money = count_days * money_per_day
profit = money - (money/8)

print(profit)
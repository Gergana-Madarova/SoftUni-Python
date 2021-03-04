price_of_excursion = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_of_puzzle = 2.6
price_of_doll = 3
price_of_bear = 4.1
price_of_minion = 8.2
price_of_truck = 2

sum_toys = count_trucks + count_bears + count_dolls + count_minions + count_puzzles
total_cost = price_of_puzzle * count_puzzles + price_of_doll * count_dolls + price_of_bear * count_bears + price_of_minion * count_minions + price_of_truck * count_trucks

if sum_toys >= 50:
    total_cost = total_cost - (0.25 * total_cost)

total_cost = total_cost - (0.1 * total_cost)

if total_cost >= price_of_excursion:
    print(f'Yes! {total_cost - price_of_excursion:.2f} lv left.')
elif total_cost < price_of_excursion:
    print(f'Not enough money! {price_of_excursion - total_cost:.2f} lv needed.')
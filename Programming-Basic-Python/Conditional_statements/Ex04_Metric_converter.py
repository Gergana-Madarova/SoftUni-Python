number = float(input())
metric_from = input()
metric_to = input()

# number in m
if metric_from == 'mm':
    number = number / 1000
elif metric_from == 'cm':
    number = number / 100

if (metric_to == 'cm'):
    number = number * 100
elif (metric_to == 'mm'):
    number = number * 1000

print(f'{number:.3f}')

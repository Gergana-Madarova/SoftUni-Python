deposit = float(input())
term = int(input())
annual_interest_rate = float(input())

sum = deposit + term * ((deposit * annual_interest_rate / 100) / 12)

print(sum)
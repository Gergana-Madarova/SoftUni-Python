kvm = float(input())

final_price = kvm * 7.61
discount = 0.18 * final_price
final_price -= discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
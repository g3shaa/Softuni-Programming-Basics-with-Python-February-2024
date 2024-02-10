square_meters = float(input())

price_per_square_meter = 7.61
total_price = square_meters * price_per_square_meter
discount = total_price * 0.18
final_price = total_price - discount

print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")

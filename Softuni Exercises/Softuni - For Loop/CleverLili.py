age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved = 0
toys_count = 0
money_gift = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money_gift += 10
        money_saved += money_gift
        money_saved -= 1  # Brother's money
    else:
        toys_count += 1

money_from_toys = toys_count * toy_price
total_money_saved = money_saved + money_from_toys

if total_money_saved >= washing_machine_price:
    print(f"Yes! {total_money_saved - washing_machine_price:.2f}")
else:
    needed_money = washing_machine_price - total_money_saved
    print(f"No! {needed_money:.2f}")

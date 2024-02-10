budget = float(input())
counter = 0
total_price = 0

while True:
    product = input()
    if product == "Stop":
        break
    price = float(input())
    counter += 1

    if counter % 3 == 0:
        price /= 2

    total_price += price
    if total_price > budget:
        print("You don't have enough money!")
        print(f"You need {total_price - budget:.2f} leva!")
        break

if total_price <= budget:
    print(f"You bought {counter} products for {total_price:.2f} leva.")

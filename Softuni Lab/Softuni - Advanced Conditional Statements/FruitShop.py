fruit = input()
day = input()
quantity = float(input())

working_days_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit in working_days_prices:
        total_price = working_days_prices[fruit] * quantity
        print(f"{total_price:.2f}")
    else:
        print("error")
elif day in ["Saturday", "Sunday"]:
    if fruit in weekend_prices:
        total_price = weekend_prices[fruit] * quantity
        print(f"{total_price:.2f}")
    else:
        print("error")
else:
    print("error")

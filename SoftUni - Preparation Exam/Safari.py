budget = float(input())
fuel_liters = float(input())
day_of_week = input()

fuel_cost = fuel_liters * 2.10
guide_cost = 100
total_cost = fuel_cost + guide_cost

if day_of_week == "Saturday":
    total_cost *= 0.9
elif day_of_week == "Sunday":
    total_cost *= 0.8

if budget >= total_cost:
    money_left = budget - total_cost
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_needed = total_cost - budget
    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")

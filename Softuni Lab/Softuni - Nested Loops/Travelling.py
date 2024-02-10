destination = input()

while destination != "End":
    min_budget = float(input())
    saved_money = 0

    while saved_money < min_budget:
        current_savings = float(input())
        saved_money += current_savings

    print(f"Going to {destination}!")
    destination = input()

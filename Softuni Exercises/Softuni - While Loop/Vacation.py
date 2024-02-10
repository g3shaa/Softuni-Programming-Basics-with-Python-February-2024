needed_money = float(input())
money = float(input())
spend = 0
days = 0

while money < needed_money:
    save_spend = input()
    amount = float(input())
    days += 1
    if save_spend.lower() == "save":
        money += amount
        spend = 0
    elif save_spend.lower() == "spend":
        if amount >= money:
            money = 0
        else:
            money -= amount
        spend += 1
        if spend == 5:
            break

if money >= needed_money:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can't save the money.\n{days}")
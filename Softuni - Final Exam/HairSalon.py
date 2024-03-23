target = int(input())
total_money = 0

while total_money < target:
    command = input()
    if command == "closed":
        break
    
    if command == "haircut":
        service = input()
        if service == "mens":
            total_money += 15
        elif service == "ladies":
            total_money += 20
        elif service == "kids":
            total_money += 10
    elif command == "color":
        service = input()
        if service == "touch up":
            total_money += 20
        elif service == "full color":
            total_money += 30

if total_money >= target:
    print("You have reached your target for the day!")
else:
    needed_money = target - total_money
    print(f"Target not reached! You need {needed_money}lv. more.")

print(f"Earned money: {total_money}lv.")

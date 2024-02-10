day = input()

ticket_prices = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16
}

if day in ticket_prices:
    print(ticket_prices[day])
else:
    print("Invalid day")

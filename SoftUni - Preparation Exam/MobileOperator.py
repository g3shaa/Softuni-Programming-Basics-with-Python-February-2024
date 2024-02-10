contract_length = input()
contract_type = input()
mobile_internet = input()
months = int(input())

prices = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99
    },
    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79
    }
}

internet_prices = {
    "Small": {"yes": 5.50, "no": 0},
    "Middle": {"yes": 4.35, "no": 0},
    "Large": {"yes": 4.35, "no": 0},
    "ExtraLarge": {"yes": 3.85, "no": 0}
}

total_price = prices[contract_length][contract_type]

total_price += internet_prices[contract_type][mobile_internet]

if contract_length == "two":
    total_price *= 0.9625 

total_price *= months  

print(f"{total_price:.2f} lv.")

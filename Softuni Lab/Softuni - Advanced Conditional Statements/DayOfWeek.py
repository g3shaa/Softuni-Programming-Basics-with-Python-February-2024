day_number = int(input())

day_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

day = day_dict.get(day_number, "Error")
print(day)

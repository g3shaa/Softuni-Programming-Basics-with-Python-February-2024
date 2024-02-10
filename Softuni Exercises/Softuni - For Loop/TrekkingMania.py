groups_count = int(input())
total_people = 0

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(groups_count):
    group_size = int(input())
    total_people += group_size

    if 1 <= group_size <= 5:
        musala_count += group_size
    elif 6 <= group_size <= 12:
        monblan_count += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro_count += group_size
    elif 26 <= group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size

musala_percent = (musala_count / total_people) * 100
monblan_percent = (monblan_count / total_people) * 100
kilimanjaro_percent = (kilimanjaro_count / total_people) * 100
k2_percent = (k2_count / total_people) * 100
everest_percent = (everest_count / total_people) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")

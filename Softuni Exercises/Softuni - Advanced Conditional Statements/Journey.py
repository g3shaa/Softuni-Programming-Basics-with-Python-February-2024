budget = float(input())
season = input()

destination = ''
rest_type = ''
percent = 0

if budget <= 100:
    destination = 'Bulgaria'
    rest_type = 'Camp'
    percent = 30
    if season == 'winter':
        rest_type = 'Hotel'
        percent = 70

elif budget <= 1000:
    destination = 'Balkans'
    rest_type = 'Camp'
    percent = 40
    if season == 'winter':
        rest_type = 'Hotel'
        percent = 80

else:
    destination = 'Europe'
    rest_type = 'Hotel'
    percent = 90

cost = budget * percent / 100

print(f"Somewhere in {destination}")
print(f"{rest_type} - {cost:.2f}")
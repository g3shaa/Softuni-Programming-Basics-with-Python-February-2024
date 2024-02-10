from math import floor
count_tournaments = int(input())
starting_points = float(input())
temp_points = 0
countW = 0
for i in range(count_tournaments):
        res = input()
        if res == "W":
            temp_points += 2000
            countW += 1
        if res == "F":
            temp_points += 1200
        if res == "SF":
            temp_points += 720
final_points = starting_points + temp_points
avg_points = temp_points / count_tournaments
winning = countW / count_tournaments * 100

print(f'Final points: {floor(final_points)}')
print(f'Average points: {floor(avg_points)}')
print(f'{winning:.2f}%')
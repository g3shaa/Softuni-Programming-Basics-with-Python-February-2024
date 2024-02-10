hour = int(input())
minutes = int(input())

minutes += 15

if minutes // 60:
    minutes = minutes % 60
    hour += 1

if hour > 23:
    hour = 0

print(f"{hour}:{minutes:02d}")
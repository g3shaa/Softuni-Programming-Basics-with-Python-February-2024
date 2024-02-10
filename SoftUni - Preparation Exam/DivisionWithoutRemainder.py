n = int(input())

count_divisible_by_2 = 0
count_divisible_by_3 = 0
count_divisible_by_4 = 0

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        count_divisible_by_2 += 1
    if number % 3 == 0:
        count_divisible_by_3 += 1
    if number % 4 == 0:
        count_divisible_by_4 += 1

percentage_divisible_by_2 = (count_divisible_by_2 / n) * 100
percentage_divisible_by_3 = (count_divisible_by_3 / n) * 100
percentage_divisible_by_4 = (count_divisible_by_4 / n) * 100

print(f"{percentage_divisible_by_2:.2f}%")
print(f"{percentage_divisible_by_3:.2f}%")
print(f"{percentage_divisible_by_4:.2f}%")
start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination_found = False
combination_count = 0

for i in range(start_interval, end_interval + 1):
    for j in range(start_interval, end_interval + 1):
        combination_count += 1
        if i + j == magic_number:
            combination_found = True
            print(f"Combination N:{combination_count} ({i} + {j} = {magic_number})")
            break

if not combination_found:
    print(f"{combination_count} combinations - neither equals {magic_number}")

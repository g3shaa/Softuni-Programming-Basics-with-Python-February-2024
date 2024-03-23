def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_pins(first_range, second_range, third_range):
    pins = []
    for i in range(2, first_range + 1, 2):
        for j in range(2, second_range + 1):
            if is_prime(j):
                for k in range(2, third_range + 1, 2):
                    pins.append((i, j, k))
    return pins

first_range = int(input())
second_range = int(input())
third_range = int(input())

valid_pins = generate_pins(first_range, second_range, third_range)
for pin in valid_pins:
    print(' '.join(map(str, pin)))
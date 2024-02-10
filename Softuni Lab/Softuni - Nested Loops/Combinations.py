import math

def calculate_combinations(n, k):
    return math.comb(n + k - 1, k - 1)

n = int(input())
result = calculate_combinations(n, 3)
print(result)

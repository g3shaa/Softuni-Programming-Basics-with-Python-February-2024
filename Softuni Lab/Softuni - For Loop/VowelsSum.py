text = input().lower()

vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
total_value = 0

for char in text:
    if char in vowel_values:
        total_value += vowel_values[char]

print(total_value)

# Входни данни
rolls_of_paper = int(input())
rolls_of_cloth = int(input())
liters_of_glue = float(input())
discount_percent = int(input())

# Цени на материалите
price_per_roll_of_paper = 5.80
price_per_roll_of_cloth = 7.20
price_per_liter_of_glue = 1.20

# Изчисления
total_price = (rolls_of_paper * price_per_roll_of_paper) + (rolls_of_cloth * price_per_roll_of_cloth) + (liters_of_glue * price_per_liter_of_glue)
discounted_price = total_price - (total_price * (discount_percent / 100))

# Изход
print(f"{discounted_price:.3f}")

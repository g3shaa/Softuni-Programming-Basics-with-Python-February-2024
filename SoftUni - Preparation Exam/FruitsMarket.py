strawberry_price_per_kg = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())

raspberry_price_per_kg = strawberry_price_per_kg / 2
orange_price_per_kg = raspberry_price_per_kg * 0.6
banana_price_per_kg = raspberry_price_per_kg * 0.2

total_cost = (strawberry_price_per_kg * strawberry_kg) + (banana_price_per_kg * banana_kg) + (orange_price_per_kg * orange_kg) + (raspberry_price_per_kg * raspberry_kg)

print(f'{total_cost:.2f}')

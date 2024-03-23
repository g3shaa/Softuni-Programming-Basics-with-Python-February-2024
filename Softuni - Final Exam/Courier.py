weight = float(input())
type = input().lower()
distance = int(input())
price_per_kilometer = 0.0
result = 0.0
result1 = 0.0
up = 0.0
up2 = 0.0
up3 = 0.0

if type == "standard":
    if weight < 1.0:
        price_per_kilometer = 0.03
        result = distance * price_per_kilometer
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 1 <= weight <= 10:
        price_per_kilometer = 0.05
        result = distance * price_per_kilometer
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 11 <= weight <= 40:
        price_per_kilometer = 0.10
        result = distance * price_per_kilometer
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 41 <= weight <= 90:
        price_per_kilometer = 0.15
        result = distance * price_per_kilometer
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 91 <= weight <= 150:
        price_per_kilometer = 0.20
        result = distance * price_per_kilometer
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
elif type == "express":
    if weight < 1.0:
        price_per_kilometer = 0.03
        result1 = distance * price_per_kilometer
        up = 0.80 * price_per_kilometer
        up2 = distance * up
        up3 = weight * up2
        result = result1 + up3
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 1 <= weight <= 10:
        price_per_kilometer = 0.05
        result1 = distance * price_per_kilometer
        up = 0.40 * price_per_kilometer
        up2 = distance * up
        up3 = weight * up2
        result = result1 + up3
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 11 <= weight <= 40:
        price_per_kilometer = 0.10
        result1 = distance * price_per_kilometer
        up = 0.05 * price_per_kilometer
        up2 = distance * up
        up3 = weight * up2
        result = result1 + up3
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 41 <= weight <= 90:
        price_per_kilometer = 0.15
        result1 = distance * price_per_kilometer
        up = 0.02 * price_per_kilometer
        up2 = distance * up
        up3 = weight * up2
        result = result1 + up3
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")
    elif 91 <= weight <= 150:
        price_per_kilometer = 0.20
        result1 = distance * price_per_kilometer
        up = 0.01 * price_per_kilometer
        up2 = distance * up
        up3 = weight * up2
        result = result1 + up3
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {result:.2f} lv.")

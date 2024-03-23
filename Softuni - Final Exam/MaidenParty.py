party_price = float(input())
love_messages = int(input())
wax_roses = int(input())
keychains = int(input())
caricatures = int(input())
luck_surprises = int(input())

love_message_price = 0.60
wax_rose_price = 7.20
keychain_price = 3.60
caricature_price = 18.20
luck_surprise_price = 22

total_price = (love_messages * love_message_price) + (wax_roses * wax_rose_price) + (keychains * keychain_price) + (caricatures * caricature_price) + (luck_surprises * luck_surprise_price)

if love_messages + wax_roses + keychains + caricatures + luck_surprises >= 25:
    total_price -= total_price * 0.35

total_price -= total_price * 0.10  # 10% hosting fee

if total_price >= party_price:
    left_money = total_price - party_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = party_price - total_price
    print(f"Not enough money! {needed_money:.2f} lv needed.")

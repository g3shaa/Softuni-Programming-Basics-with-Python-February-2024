w = int(input())
l = int(input())
cake_pieces = w * l
cake_over = False
command = input()
while command != "STOP":
    current_num_pieces = int(command)
    cake_pieces -= current_num_pieces
    if cake_pieces < 0:
        cake_over = True
        break
    command = input()
if cake_over:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
else:
    print(f"{cake_pieces} pieces are left.")
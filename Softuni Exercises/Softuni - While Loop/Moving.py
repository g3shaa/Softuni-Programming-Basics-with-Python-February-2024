w = int(input())
l = int(input())
h = int(input())
total = w * l * h
is_there_space = True
command = input()
while command != "Done":
    number_of_boxes = int(command)
    total -= number_of_boxes
    if total < 0:
        is_there_space = False
        break
    command = input()
if is_there_space:
    print(f"{total} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total)} Cubic meters more.")
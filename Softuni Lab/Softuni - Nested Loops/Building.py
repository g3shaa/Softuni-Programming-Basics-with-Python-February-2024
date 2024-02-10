floors = int(input())
rooms_per_floor = int(input())

for floor in range(floors, 0, -1):
    for room in range(rooms_per_floor):
        if floor == floors:
            room_type = "L"
        else:
            room_type = "A" if floor % 2 != 0 else "O"
        print(f"{room_type}{floor}{room}", end=" ")
    print()

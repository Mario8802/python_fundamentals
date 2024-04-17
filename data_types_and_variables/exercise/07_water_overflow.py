WATER_TANK = 255
current_water_tank = 0
n = int(input())

for nothing in range(n):
    liters_of_water = int(input())
    if 0 >= liters_of_water <= 20:
        exit()
    if current_water_tank + liters_of_water > WATER_TANK:
        print("Insufficient capacity!")
    else:
        current_water_tank += liters_of_water

print(current_water_tank)

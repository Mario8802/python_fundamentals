def drive_car(car, distance, fuel):
    if cars[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars[car]["mileage"] += distance
        cars[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

def refuel_car(car, fuel):
    if fuel + cars[car]["fuel"] > 75:
        fuel_added = 75 - cars[car]["fuel"]
        cars[car]["fuel"] = 75
    else:
        fuel_added = fuel
        cars[car]["fuel"] += fuel
    print(f"{car} refueled with {fuel_added} liters")

def revert_mileage(car, kilometers):
    if cars[car]["mileage"] - kilometers < 10000:
        cars[car]["mileage"] = 10000
    else:
        cars[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")

n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    action, car = command[0], command[1]
    if action == "Drive":
        distance, fuel = int(command[2]), int(command[3])
        drive_car(car, distance, fuel)
    elif action == "Refuel":
        fuel = int(command[2])
        refuel_car(car, fuel)
    elif action == "Revert":
        kilometers = int(command[2])
        revert_mileage(car, kilometers)

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")


n = int(input())
cars = {}

# Collecting initial car information
for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

# Processing commands
while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    action, car = command[0], command[1]
    if action == "Drive":
        distance, fuel = int(command[2]), int(command[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif action == "Refuel":
        fuel = int(command[2])
        if fuel + cars[car]["fuel"] > 75:
            fuel_added = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
        else:
            fuel_added = fuel
            cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel_added} liters")
    elif action == "Revert":
        kilometers = int(command[2])
        if cars[car]["mileage"] - kilometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

# Printing final car information
for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")

cities = {}
# Collecting cities information
command = input().split("||")
while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
        # {"Tortuga": {"population": 0, "gold": 0}}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split("||")
# Doing events
command = input().split("=>")
while command[0] != "End":
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input().split("=>")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, town_information in cities.items():
        print(f'{town} -> Population: {town_information["population"]} citizens, Gold: {town_information["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


#island-Tortuga,Haiti


my_cities = {}

while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break

    city_name = command[0].strip()
    population = int(command[1].strip())
    gold = int(command[2].strip())

    if city_name not in my_cities:
        my_cities[city_name] = {'population': population, 'gold': gold}
    else:
        my_cities[city_name]['population'] += population
        my_cities[city_name]['gold'] += gold

while True:
    text = input()
    if text == "End":
        break

    action, *args = text.split("=>")
    if action == "Plunder":
        town, people, gold = args
        people = int(people)
        gold = int(gold)
        my_cities[town]['population'] -= people
        my_cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if my_cities[town]['population'] <= 0 or my_cities[town]['gold'] <= 0:
            del my_cities[town]
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town, gold = args
        gold = int(gold)
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            my_cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {my_cities[town]['gold']} gold.")

print(f"Ahoy, Captain! There are {len(my_cities)} wealthy settlements to go to:")
for town, data in my_cities.items():
    print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")

=========================================================================================================


from collections import defaultdict

cities = defaultdict(lambda: {"population": 0, "gold": 0})

# Collecting cities information
command = input().split("||")
while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split("||")

# Doing events
command = input().split("=>")
while command[0] != "End":
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input().split("=>")

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, town_information in cities.items():
        print(f"{town} -> Population: {town_information['population']} citizens, Gold: {town_information['gold']} kg")


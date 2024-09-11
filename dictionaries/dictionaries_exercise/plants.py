def rate(plant_data, plant, rating):
    if plant in plant_data:
        plant_data[plant]['ratings'].append(int(rating))
    else:
        print("error")


def update(plant_data, plant, new_rarity):
    if plant in plant_data:
        plant_data[plant]['rarity'] = int(new_rarity)
    else:
        print("error")


def reset(plant_data, plant):
    if plant in plant_data:
        plant_data[plant]['ratings'] = []
    else:
        print("error")


def plant_discovery(n):
    plant_data = {}

    # Input the plants and their rarities
    for _ in range(n):
        plant, rarity = input().split("<->")
        plant_data[plant] = {'rarity': int(rarity), 'ratings': []}

    # Handle commands until "Exhibition"
    while True:
        command = input()
        if command == "Exhibition":
            break

        command_parts = command.split(": ")
        action = command_parts[0]
        details = command_parts[1].split(" - ")

        plant = details[0]
        if action == "Rate":
            rating = details[1]
            rate(plant_data, plant, rating)
        elif action == "Update":
            new_rarity = details[1]
            update(plant_data, plant, new_rarity)
        elif action == "Reset":
            reset(plant_data, plant)

    # Exhibition Output
    print("Plants for the exhibition:")
    for plant, info in plant_data.items():
        average_rating = sum(info['ratings']) / len(info['ratings']) if info['ratings'] else 0
        print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")


# Input the number of plants
n = int(input())
plant_discovery(n)

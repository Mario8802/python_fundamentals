items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
for material, quantity in items.items():
    print(f"{material}: {quantity}")



# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
#     • "Shadowmourne" - requires 250 Shards
#     • "Valanyr" - requires 250 Fragments
#     • "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

# Output
#     • On the first line, print the obtained item in the format: "{Legendary item} obtained!"
#     • On the next three lines, print the remaining key materials
#     • On the several final lines, print the junk items
#     • All materials should be printed in the format: "{material}: {quantity}"
#     • The output should be lowercase, except for the first letter of the legendary



def obtain_legendary_item():
    materials = {"shards": 0, "fragments": 0, "motes": 0}
    junk = {}
    input_order = []

    legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

    while True:
        data = input().lower().split()
        for i in range(0, len(data), 2):
            quantity = int(data[i])
            material = data[i + 1]
            input_order.append(material)

            if material in materials:
                materials[material] += quantity

                if materials[material] >= 250:
                    print(f"{legendary_items[material]} obtained!")
                    materials[material] -= 250
                    # Print remaining materials
                    print_materials(materials, junk)
                    return
            else:
                if material in junk:
                    junk[material] += quantity
                else:
                    junk[material] = quantity

def print_materials(materials, junk):
    # Define the materials to be tracked in the order specified
    tracked_materials = ["shards", "fragments", "motes"]

    for material in tracked_materials:
        if material in materials:
            print(f"{material}: {materials[material]}")

    
    for item, quantity in junk.items():
        print(f"{item}: {quantity}")


obtain_legendary_item()

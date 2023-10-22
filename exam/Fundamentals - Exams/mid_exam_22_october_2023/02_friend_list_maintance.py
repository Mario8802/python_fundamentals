friends = input().split(", ")
action = input()
lost_names = 0
blacklisted_names = 0

while action != "Report":
    command = action.split()[0]
    if command == "Blacklist":
        name = action.split()[1]
        if name not in friends:
            print(f'{name} was not found.')
        else:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            print(f'{name} was blacklisted.')
            blacklisted_names += 1
    elif command == "Error":
        index = int(action.split()[1])
        name = friends[index]
        if name != "Blacklisted" and name != "Lost":
            friends[index] = "Lost"
            print(f"{name} was lost due to an error.")
            lost_names += 1
    elif command == "Change":
        index = int(action.split()[1])
        name = action.split()[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {name}.")
            friends[index] = name
    action = input()

print(f'Blacklisted names: {blacklisted_names}')
print(f'Lost names: {lost_names}')
print(' '.join(friends))
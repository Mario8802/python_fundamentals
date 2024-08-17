def heal_player(health, number):
    healed_amount = min(100 - health, number)
    health += healed_amount
    print(f"You healed for {healed_amount} hp.")
    print(f"Current health: {health} hp.")
    return health


def find_bitcoins(bitcoins, number):
    bitcoins += number
    print(f"You found {number} bitcoins.")
    return bitcoins


def fight_monster(health, action, number, count_rooms):
    health -= number
    if health > 0:
        print(f"You slayed {action}.")
    else:
        print(f"You died! Killed by {action}.")
        print(f"Best room: {count_rooms}")
    return health


def main():
    health = 100
    bitcoins = 0
    is_dead = False
    rooms = input().split('|')
    count_rooms = 0

    for room in rooms:
        count_rooms += 1
        action, number = room.split()
        number = int(number)

        if action == "potion":
            health = heal_player(health, number)

        elif action == "chest":
            bitcoins = find_bitcoins(bitcoins, number)

        else:
            health = fight_monster(health, action, number, count_rooms)
            if health <= 0:
                is_dead = True
                break

    if not is_dead:
        print("You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {health}")


main()


#without functions 
health = 100
bitcoins = 0
is_dead = False
rooms = input().split('|')
count_rooms = 0

for room in rooms:
    count_rooms += 1
    action, number = room.split()
    number = int(number)
    
    if action == "potion":
        healed_amount = min(100 - health, number)
        health += healed_amount
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    
    elif action == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    
    else:
        health -= number
        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {count_rooms}")
            is_dead = True
            break

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

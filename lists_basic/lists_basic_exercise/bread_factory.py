working_day_events = input().split("|")

energy = 100
coins = 100
close_condition = False

for event in working_day_events:
    event_details = event.split('-')
    event_name = event_details[0]
    number = int(event_details[1])

    if event_name == "rest":
        if energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")

        print(f"Current energy: {energy}.")

    elif event_name == "order":
        if energy >= 30:
            print(f"You earned {number} coins.")
            energy -= 30
            coins += number
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            print(f"You bought {event_name}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {event_name}.")
            close_condition = True
            break

if not close_condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

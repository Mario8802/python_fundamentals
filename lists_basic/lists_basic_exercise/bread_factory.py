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


================================================================================


working_day_events = input().split("|")

energy = 100
coins = 100
gained_energy = 0
earned_coins = 0
ingredients = []
job_done = False

for event in working_day_events:
    event_details = event.split('-')
    event_name = event_details[0]
    number = int(event_details[1])

    if event_name == "rest":
        if energy + number <= 100:
            energy += number
            gained_energy = number  
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            gained_energy = 100 - energy  0
            energy = 100
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
    elif event_name == "order":
        energy -= 30
        if energy >= 0:
            coins += number
            earned_coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            job_done = True
            continue  
    else:
        if coins - number >= 0:
            ingredients.append(event_name)
            coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            job_done = True
            break

if not job_done:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

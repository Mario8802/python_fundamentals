def rate_function(plant, rating, plant_rating):

    if plant in plant_rating:
        plant_rating[plant].append(rating)

    else:
        print('error')

    return plant_rating


def update_function(plant, new_rarity, plant_rarity):

    if plant in plant_rarity:
        plant_rarity[plant] = new_rarity

    else:
        print('error')

    return plant_rarity


def reset_function(plant, plant_ratings):

    if plant in plant_ratings:
        plant_ratings[plant].clear()

    else:
        print('error')

    return plant_ratings


def plant_command(plant_rarity, plant_rating):
    while True:
        command_one = input()

        if command_one == 'Exhibition':
            break

        command_one = command_one.split(': ')
        command_two = command_one[1].split(' - ')
        plant = command_two[0]

        if 'Rate' in command_one:
            rating = int(command_two[1])
            rate_function(plant, rating, plant_rating)

        elif 'Update' in command_one:
            new_rarity = int(command_two[1])
            update_function(plant, new_rarity, plant_rarity)

        elif 'Reset' in command_one:
            reset_function(plant, plant_rating)


def plant_discovery_information():
    n = int(input())

    plant_rarity_info = {}
    plant_rating_info = {}

    for _ in range(n):
        input_line = input().split('<->')
        plant = input_line[0]

        rarity = int(input_line[1])
        plant_rarity_info[plant] = rarity

        plant_rating_info[plant] = []

    plant_command(plant_rarity_info, plant_rating_info)

    print('Plants for the exhibition:')

    for plant_name1, rarity_1 in plant_rarity_info.items():

        if len(plant_rating_info[plant_name1]) <= 0:
            average_rating = 0

        else:
            average_rating = sum(plant_rating_info[plant_name1]) / len(plant_rating_info[plant_name1])

        print(f'- {plant_name1}; Rarity: {rarity_1}; Rating: {average_rating:.2f}')


plant_discovery_information()
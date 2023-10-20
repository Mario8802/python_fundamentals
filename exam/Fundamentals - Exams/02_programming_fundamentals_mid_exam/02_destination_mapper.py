import re


def calculate_points(destinations):
    travel_points = 0
    locations = []

    for places in destinations:
        travel_points += len(places.group(2))
        locations.append(places.group(2))

    return travel_points, ', '.join(locations)


text = input()

pattern = r'([=|/])([A-Z][A-Za-z]{2,})\1'
valid_ones = re.finditer(pattern, text)
points, names = calculate_points(valid_ones)

print(f'Destinations: {names}')
print(f'Travel Points: {points}')
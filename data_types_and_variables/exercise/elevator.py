from math import ceil


people = int(input())
capacity = int(input())
count_trips = ceil(people / capacity)

print(count_trips)

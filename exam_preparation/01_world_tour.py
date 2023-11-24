def add_stop(stops, index, some_string):
    if index in range(len(stops)):
        stops = stops[:index] + some_string + stops[index:]
    return stops


def remove_stop(stops, start_index, end_index):
    if start_index in range(len(stops)) and end_index in range(len(stops)):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch(stops, old_string, new_string):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


stops = input()
command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        index, some_string = int(command[1]), command[2]
        stops = add_stop(stops, index, some_string)
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)
    command = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")




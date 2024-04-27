number = int(input())
wagons = [0] * number

while True:
    command = input()

    if command == 'End':
        break

    data = command.split()
    current_command = data[0]

    if current_command == 'add':
        people_to_add = data[1]
        wagons[-1] += int(people_to_add)

    elif current_command == 'insert':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people

    elif current_command == 'leave':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people

print(wagons)



======================================================================


wagons = int(input())

# Initialize train list with zeros
train = [0] * wagons

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "add":
        # Add people to the last wagon
        train[-1] += int(command[1])
    elif command[0] == "insert":
        # Insert people at the specified wagon
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command[0] == "leave":
        # Remove people from the specified wagon
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

# Print the train
print(train)

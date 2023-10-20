destination = input()

while True:
    command = input()

    if command == 'Travel':
        break

    command = command.split(':')

    if 'Add Stop' in command:
        index = int(command[1])
        text = command[2]
        destination = list(destination)

        if -1 < index < len(destination):
            destination.insert(index, text)
        destination = ''.join(destination)
        print(destination)

    elif 'Remove Stop' in command:

        first_index = int(command[1])
        last_index = int(command[2])

        if -1 < first_index < len(destination) and -1 < last_index < len(destination):
            destination = destination[:first_index] + destination[last_index + 1:]
            
        print(destination)

    elif 'Switch' in command:

        old_text = command[1]
        new_text = command[2]
        destination = destination.replace(old_text, new_text)

        print(destination)

print(f'Ready for world tour! Planned stops: {destination}')
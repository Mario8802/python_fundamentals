array = input().split()
command = input()

while command != 'end':
    command = command.split()
    if 'swap' in command:
        index_one = int(command[1])
        index_two = int(command[2])
        number_on_index_one = array[index_one]
        array[index_one] = array[index_two]
        array[index_two] = number_on_index_one

    elif 'multiply' in command:
        index_one = int(command[1])
        index_two = int(command[2])
        result = int(array[index_one]) * int(array[index_two])
        array.pop(index_one)
        array.insert(index_one, str(result))

    elif 'decrease' in command:
        for i in range(len(array)):
            current_number = int(array[i])
            current_number -= 1
            array[i] = str(current_number)

    command = input()

print(', '.join(array))
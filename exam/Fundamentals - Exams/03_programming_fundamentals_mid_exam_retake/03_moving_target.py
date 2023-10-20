the_sequence_of_targets = [int(number) for number in input().split()]
command = input()

while command != 'End':
    command = command.split()

    if 'Shoot' in command:
        index = int(command[1])
        power = int(command[2])

        if 0 <= index < len(the_sequence_of_targets):
            for element, string in enumerate(the_sequence_of_targets):

                if element == index:
                    string = int(string)
                    string -= power
                    the_sequence_of_targets[index] = string

            if the_sequence_of_targets[index] <= 0:
                the_sequence_of_targets.pop(index)

    elif 'Add' in command:
        index = int(command[1])
        value = int(command[2])

        if 0 <= index < len(the_sequence_of_targets):
            the_sequence_of_targets.insert(index, value)

        else:
            print("Invalid placement!")

    elif 'Strike' in command:
        index = int(command[1])
        radius = int(command[2])
        idx_before = index - radius
        idx_after = index + radius

        if (0 <= idx_before < len(the_sequence_of_targets)
                and 0 <= index < len(the_sequence_of_targets)
                and 0 <= idx_after < len(
                the_sequence_of_targets)):

            the_sequence_of_targets = the_sequence_of_targets[:idx_before] + the_sequence_of_targets[the_one_after_it + 1:]

        else:
            print("Strike missed!" )

    command = input()

the_sequence_of_targets = list(map(str, the_sequence_of_targets))

print('|'.join(the_sequence_of_targets))
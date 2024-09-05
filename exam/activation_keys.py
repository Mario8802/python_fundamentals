def contains_substring(activation_key, substring):
    if substring in activation_key:
        print(f"{activation_key} contains {substring}")
    else:
        print("Substring not found!")


def flip_case(activation_key, case, start_index, end_index):
    part_before = activation_key[:start_index]
    part_after = activation_key[end_index:]

    if case == "Upper":
        modified_part = activation_key[start_index:end_index].upper()
    elif case == "Lower":
        modified_part = activation_key[start_index:end_index].lower()

    return part_before + modified_part + part_after


def slice_key(activation_key, start_index, end_index):
    part_before = activation_key[:start_index]
    part_after = activation_key[end_index:]

    return part_before + part_after


def process_commands(activation_key):
    while True:
        command = input().split('>>>')

        if command[0] == 'Generate':
            break

        elif command[0] == 'Contains':
            substring = command[1]
            contains_substring(activation_key, substring)

        elif command[0] == 'Flip':
            case = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            activation_key = flip_case(activation_key, case, start_index, end_index)
            print(activation_key)

        elif command[0] == 'Slice':
            start_index = int(command[1])
            end_index = int(command[2])
            activation_key = slice_key(activation_key, start_index, end_index)
            print(activation_key)

    return activation_key


activation_key = input()
activation_key = process_commands(activation_key)
print(f"Your activation key is: {activation_key}")

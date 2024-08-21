def move(text, number_of_letters):
    first_part = text[:number_of_letters]
    second_part = text[number_of_letters:]
    modified_text = second_part + first_part
    return modified_text


def insert(text, index, value):
    return text[:index] + value + text[index:]

def change_all_occurrences(text, substring, replacement):
    return text.replace(substring, replacement)

message = input()

while True:
    command = input().split('|')

    if command[0] == 'Decode':
        break

    if command[0] == 'Move':
        number_of_letters = int(command[1])
        message = move(message, number_of_letters)

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message = insert(message, index, value)

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = change_all_occurrences(message, substring, replacement)

print(f"The decrypted message is: {message}")

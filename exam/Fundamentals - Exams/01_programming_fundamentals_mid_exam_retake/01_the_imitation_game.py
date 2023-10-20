text = input()

while True:
    command = input()

    if command == 'Decode':
        break

    command = command.split('|')

    if 'Move' in command:
        number_of_letters = int(command[1])

        text = list(text)
        text[number_of_letters:], text[:number_of_letters] = text[:number_of_letters], text[number_of_letters:]
        text = ''.join(text)

    if 'Insert' in command:
        text = list(text)
        index = int(command[1])
        value = command[2]
        text.insert(index, value)
        text = ''.join(text)

    if 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        text = text.replace(substring, replacement)

print(f'The decrypted message is: {text}')
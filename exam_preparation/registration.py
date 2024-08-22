def letters(username, action):
    if action == 'Lower':
        username = username.lower()
    elif action == 'Upper':
        username = username.upper()
    print(username)
    return username


def reverse(text, index1, index2):
    if 0 > index1 or 0 > index2 or index1 > len(text) or index2 >= len(text):
        return
    substring = text[index1:index2 + 1]
    print(substring[::-1])


def substring(text, substring):
    if substring in text:
        text = text.replace(substring, '')
        print(text)
    else:
        print(f"The username {text} doesn't contain {substring}.")
    return text


def replace(text, character):
    text = text.replace(character, '-')
    print(text)
    return text


def isvalid(text, character):
    if character in text:
        print("Valid username.")
    else:
        print(f"{character} must be contained in your username.")


name = input()

while True:
    command = input().split()

    if command[0] == 'Registration':
        break

    elif command[0] == 'Letters':
        name = letters(name, command[1])

    elif command[0] == 'Reverse':
        start_index = int(command[1])
        end_index = int(command[2])
        reverse(name, start_index, end_index)

    elif command[0] == 'Substring':
        name = substring(name, command[1])

    elif command[0] == 'Replace':
        name = replace(name, command[1])

    elif command[0] == 'IsValid':
        isvalid(name, command[1])

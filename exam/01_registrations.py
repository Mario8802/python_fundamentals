username = input()

while True:
    command = input().split()

    if command[0] == "Registration":
        break

    if command[0] == "Letters":
        if command[1] == "Lower":
            username = username.lower()
            print(username)
        elif command[1] == "Upper":
            username = username.upper()
            print(username)

    elif command[0] == "Reverse":
        index1 = int(command[1])
        index2 = int(command[2])

        if index1 >= 0 and index2 < len(username):
            string_to_reverse = username[index1:index2 + 1]
            print(string_to_reverse[::-1])

    elif command[0] == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif command[0] == "Replace":
        char_to_replace = command[1]
        username = username.replace(char_to_replace, "-")
        print(username)

    elif command[0] == "IsValid":
        required_char = command[1]
        if required_char in username:
            print("Valid username.")
        else:
            print(f"{required_char} must be contained in your username.")

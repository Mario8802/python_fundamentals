def password_reset():
    password = input()

    while True:
        command = input()
        if command == "Done":
            break

        command_parts = command.split()

        if command_parts[0] == "TakeOdd":
            password = ''.join([password[i] for i in range(1, len(password), 2)])
            print(password)

        elif command_parts[0] == "Cut":
            index = int(command_parts[1])
            length = int(command_parts[2])
            password = password[:index] + password[index + length:]
            print(password)

        elif command_parts[0] == "Substitute":
            substring = command_parts[1]
            substitute = command_parts[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print("Nothing to replace!")

        else:
            print("Invalid command")

    print(f"Your password is: {password}")


password_reset()

def takeodd(password):
    new_password = password[1::2]
    print(new_password)
    return new_password


def cut(password, index, length):
    index = int(index)
    length = int(length)
    password = password[:index] + password[index+length:]
    print(password)
    return password


def substitute(password, old_element, new_element):
    if old_element in password:
        password = password.replace(old_element, new_element)
        print(password)
    else:
        print("Nothing to replace!")
    return password


def password_reset(some_string):
    password = some_string
    while True:
        command = input().split()
        if command[0] == "Done":
            break
        elif command[0] == "TakeOdd":
            password = takeodd(password)
        elif command[0] == "Cut":
            password = cut(password, command[1], command[2])
        elif command[0] == "Substitute":
            password = substitute(password, command[1], command[2])
    print(f"Your password is: {password}")


some_string = input()
password_reset(some_string)

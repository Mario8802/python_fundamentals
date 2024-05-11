while True:
    command = input()
    if command == "end":
        break
    else:
        print(f"{command} = {command[::-1]}")


while True:
    command = input()
    if command == 'end':
        break

    print(f"{command} = {command[::-1]}")
===================================================================================================================================================
class StringReverser:
    def __init__(self):
        pass

    def reverse_strings(self):
        while True:
            command = input()
            if command == 'end':
                break

            print(f"{command} = {command[::-1]}")

if __name__ == "__main__":
    reverser = StringReverser()
    reverser.reverse_strings()

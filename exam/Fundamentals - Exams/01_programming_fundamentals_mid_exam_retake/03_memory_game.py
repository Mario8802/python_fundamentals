sequence_of_elements = input().split()
moves_counter = 0
command = input()

while not command == "end":
    moves_counter += 1
    index_one = int(command.split()[0])
    index_two = int(command.split()[1])

    if (index_one == index_two or index_one < 0 or index_two < 0
            or index_one >= len(sequence_of_elements)
            or index_two >= len(sequence_of_elements)):

        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{str(moves_counter)}a")
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{str(moves_counter)}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence_of_elements[index_one] == sequence_of_elements[index_two]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index_one]}!")
        x = sequence_of_elements.pop(index_one)
        sequence_of_elements.remove(x)

    elif sequence_of_elements[index_one] != sequence_of_elements[index_two]:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {moves_counter} turns!")
        break
    command = input()

if command == "end":
    print("Sorry you lose :(\n"
          f"{' '.join(sequence_of_elements)}")
current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for character in current_string:
            new_string += character * 2

        print(new_string)

    current_string = input()

===================================================================

new_string = ""

while True:
    current_string = input()

    if current_string == "End":
        break

    if current_string != "SoftUni":
        doubled_string = ""
        for character in current_string:
            doubled_string += character * 2

        new_string += doubled_string + "\n"

print(new_string, end="")


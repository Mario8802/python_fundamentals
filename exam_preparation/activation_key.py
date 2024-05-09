activation_key = input()
is_generated = False
while activation_key != "Generate":

    instructions = input().split('>>>')
    if instructions[0] == 'Generate':
        is_generated = True
        break
    if instructions[0] == "Contains" and instructions[1] in activation_key:
        print(f"{activation_key} contains {instructions[1]}")
    elif instructions[0] == "Contains" and instructions[1] not in activation_key:
        print("Substring not found!")

    if instructions[0] == "Flip":
        if instructions[1] == "Upper":
            start_index = int(instructions[2])
            end_index = int(instructions[3])
            activation_key = (activation_key[:start_index] + activation_key[start_index:end_index].upper()
                              + activation_key[end_index:])
            print(activation_key)

        elif instructions[1] == "Lower":
            start_index = int(instructions[2])
            end_index = int(instructions[3])
            activation_key = (activation_key[:start_index] + activation_key[start_index:end_index].lower()
                              + activation_key[end_index:])
            print(activation_key)
            
    if instructions[0] == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        activation_key = (activation_key[:start_index] + activation_key[end_index:])
        print(activation_key)

if is_generated:
    print(f"Your activation key is: {activation_key}")

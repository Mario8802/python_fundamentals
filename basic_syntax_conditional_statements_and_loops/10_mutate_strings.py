# first_string = input()
# second_string = input()
# last_printed_string = first_string

# for character_index in range(len(first_string)):
#     left_part = second_string[0:character_index + 1]
#     right_part = first_string[character_index + 1:]
#     new_string = left_part + right_part
#     if new_string != last_printed_string:
#         last_printed_string = new_string
#     print(new_string)


string1 = input()
string2 = input()

# Iterate over each character index in the strings
for i in range(len(string1)):
    if string1[i] != string2[i]:
        new_string = string2[i]
        mutated_string = string1[0:i] + new_string + string1[i+1:]
        string1 = mutated_string
        print(string1)

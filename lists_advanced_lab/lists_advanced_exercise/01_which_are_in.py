first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []


for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)


===========================================================


first_string = input().split(', ')
second_string = input().split(', ')
# my_string = []

# for i in first_string:
#     for j in second_string:
#         if i in j:
#             my_string.append(i)
#             break
# print(my_string)


my_string = [i for i in first_string if any(i in j for j in second_string) ]
print(my_string)

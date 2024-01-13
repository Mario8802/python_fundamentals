number_of_strings = int(input())
for current_string in range(number_of_strings):
    pure_or_not_pure_string = input()
    if "," in pure_or_not_pure_string or \
            "." in pure_or_not_pure_string or \
            "_" in pure_or_not_pure_string:
        print(f"{pure_or_not_pure_string} is not pure!")
    else:
        print(f"{pure_or_not_pure_string} is pure.")

# n = int(input())

# for _ in range(n):
#     command = input()
#     if "," in command or "." in command or "_" in command:
#         print(f"{command} is not pure!")
#     else:
#         print(f"{command} is pure.")

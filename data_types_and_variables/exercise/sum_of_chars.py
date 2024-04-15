# number_of_characters =  int(input())
# total_sum = 0
# for character in range(number_of_characters):
#     current_character = input()
#     total_sum += ord(current_character)
# print(f"The sum equals: {total_sum}")

n = int(input())
total_sum_of_chars = 0
if 1 > n or n > 20:
    exit()

for _ in range(n):
    char = input()
    total_sum_of_chars += ord(char)
print(f"The sum equals: {total_sum_of_chars}")

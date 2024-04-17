# start_index = int(input())
# final_index = int(input())

# for number in range(start_index,final_index + 1):
#     print(chr(number), end = ' ')


start = int(input())
end = int(input())
total_sum_of_chars = ""

for char in range(start, end + 1):
    total_sum_of_chars += chr(char)
print(" ".join(total_sum_of_chars))

factor = int(input())
count = int(input())

my_list = []

for number in range(count):
    if number * factor > 0:
        my_list.append(number)
print(my_list)
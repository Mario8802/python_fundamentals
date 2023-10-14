number = int(input())
capacity = 255
total_sum = 0
for i in range(number):
    include = int(input())
    if total_sum + include > capacity:
        print("Insufficient capacity!")
    else:
        total_sum += include
print(total_sum)
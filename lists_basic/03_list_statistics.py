number = int(input())

positive = []
sum_of_negative = []

for i in range(number):
    current_number = int(input())

    if current_number >= 0 :
        positive.append(current_number)
    else:
        sum_of_negative.append(current_number)
print(positive)
print(sum_of_negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(sum_of_negative)}")
# print(f"Count of negatives: {len(sum_of_negative)}")
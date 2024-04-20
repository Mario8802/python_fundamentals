numbers_strings = input().split()

lists_with_numbers = []

for num in numbers_strings:
    lists_with_numbers.append(int(num))

count_of_numbers_to_remove = int(input())

for _ in range(count_of_numbers_to_remove):
    lists_with_numbers.remove(min(lists_with_numbers))

print(*lists_with_numbers, sep=", ")



========================================================================


nums = [int(x) for x in input().split()]
n = int(input())


for _ in range(n):
    nums.remove(min(nums))


result = ", ".join(map(str, nums))
print(result)

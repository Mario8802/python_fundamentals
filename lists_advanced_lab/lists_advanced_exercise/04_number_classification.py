def positive_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) >= 0])


def negative_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) < 0])


def even_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 == 0])


def odd_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")

==============================================================================




def positive(some_nums):
    pos_nums = [x for x in nums if x >= 0]
    return f"Positive: {', '.join(map(str,pos_nums))}"


def negative(some_nums):
    neg_nums = [x for x in nums if x < 0]
    return f"Negative: {', '.join(map(str,neg_nums))}"


def even_numbers(some_nums):
    even_nums = [x for x in nums if x % 2 == 0]
    return f"Even: {', '.join(map(str,even_nums))}"


def odd_numbers(some_nums):
    odd_nums = [x for x in nums if x % 2 != 0]
    return f"Odd: {', '.join(map(str, odd_nums))}"


nums = [int(x) for x in input().split(', ')]

print(positive(nums))
print(negative(nums))
print(even_numbers(nums))
print(odd_numbers(nums))

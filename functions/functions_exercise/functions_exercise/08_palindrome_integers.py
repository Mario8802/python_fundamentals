def is_palindrome(some_number_as_string: str) -> bool:
    return some_number_as_string == some_number_as_string[::-1]


numbers_as_string = input().split(", ")
for number_as_string in numbers_as_string:
    print(is_palindrome(number_as_string))


============================================================================


def palindrome_integers(nums):
    for num in nums:
        if num == num[::-1]:
            print(True)  # Print True if the number is a palindrome
        else:
            print(False)  # Print False if the number is not a palindrome


sequence_of_numbers = input().split(', ')
palindrome_integers(sequence_of_numbers)


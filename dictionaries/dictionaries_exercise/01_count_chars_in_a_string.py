symbols = [character for character in input() if character != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():  # if symbol not in letters
        letters[symbol] = 0
    letters[symbol] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")


# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"


def count_characters(string):
    # Remove spaces from the string
    string = string.replace(" ", "")

    # Initialize an empty dictionary to store character counts
    char_counts = {}

    # Count occurrences of each character
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Print occurrences in the specified format
    for char, count in char_counts.items():
        print(f"{char} -> {count}")


# Test the function with a sample string
sample_string = input()
count_characters(sample_string)

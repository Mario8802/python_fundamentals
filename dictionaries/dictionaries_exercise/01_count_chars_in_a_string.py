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

message = input().split()

for word in message:
    number = ''
    for char in word:
        if char.isdigit():
            number += char
    first_letter = chr(int(number))
    current_word = first_letter + word[len(number):]
    current_word = list(current_word)

    current_word[1],current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)}", end=' ')


=============================================================================



# message = input().split()
#
# for word in message:
#     number = ''
#     for char in word:
#         if char.isdigit():
#             number += char
#     first_letter = chr(int(number))
#     current_word = first_letter + word[len(number):]
#     current_word = list(current_word)
#
#     current_word[1],current_word[-1] = current_word[-1], current_word[1]
#     print(f"{''.join(current_word)}", end=' ')


# Take input message from the user
message = input().split()

# Define a function to perform the transformation on each word
def transform_word(word):
    # Extract digits from the word and concatenate them
    number = ''.join(char for char in word if char.isdigit())
    # Get the first letter of the word using the extracted number
    first_letter = chr(int(number))
    # Construct the modified word by swapping the second and last characters
    modified_word = first_letter + word[len(number):]
    modified_word = list(modified_word)
    modified_word[1], modified_word[-1] = modified_word[-1], modified_word[1]
    return ''.join(modified_word)

# Apply the transformation function to each word in the message and print the result
transformed_message = [transform_word(word) for word in message]
print(' '.join(transformed_message))

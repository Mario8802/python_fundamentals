string = input().split()
new_string = ''
for el in string:
    new_string += el * len(el)

print(new_string)

=====================================================

words = input().split()
new_words = []

for word in words:
    repeated_word = word * len(word)
    new_words.append(repeated_word)

final_string = ''.join(new_words)
print(final_string)

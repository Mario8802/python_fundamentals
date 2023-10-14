word = input()
list_from_word = [ ]
for index in range(len(word)):
    if word[index].isupper():
        list_from_word.append(index)

print(list_from_word)
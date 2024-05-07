word = input().split()

my_dictionary = {}

for w in word:
    new_word = w.lower()
    if new_word not in my_dictionary:
        my_dictionary[new_word] = 0
    my_dictionary[new_word] += 1

for k,v in my_dictionary.items():
    if v % 2 != 0:
        print(k, end=' ')

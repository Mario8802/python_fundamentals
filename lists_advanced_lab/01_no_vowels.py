text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [ch for ch in text if ch.lower() not in vowels]
print(''.join(result))

=========================================================================


my_list_with_vowels = ['a', 'o', 'u', 'e', 'i']

text = input()
word = [i for i in text if not i.lower() in my_list_with_vowels]
print("".join(word))

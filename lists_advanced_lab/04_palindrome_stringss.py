def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome_word = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f'Found palindrome {palindrome_counter} times')

===========================================================================


word = input().split()
palindrome = input()

palindromes = [w for w in word if w == w[::-1]]

print(palindromes)
print(f"Found palindrome {word.count(palindrome)} times")

============================================================================


word = input().split()
palindrome = input()
my_list_for_printing = []
my_list = []
for searcher_word in word:
    if palindrome == searcher_word:
        my_list.append(searcher_word)
    if searcher_word == searcher_word[::-1]:
        my_list_for_printing.append(searcher_word)

print(my_list_for_printing)
print(f"Found palindrome {len(my_list)} times")






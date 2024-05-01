words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))

===================================================================


word = [w for w in input().split() if len(w) % 2 == 0]

print('\n'.join(word))

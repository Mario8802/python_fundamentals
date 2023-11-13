string = input().split()
new_string = ''
for el in string:
    new_string += el * len(el)

print(new_string)
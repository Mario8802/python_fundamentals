def characters_in_range(start, end):
    result = ''
    for i in range(ord(start) + 1, ord(end)):
        result += chr(i) + ' '
    return result


start_step = input()
end_step = input()
print(characters_in_range(start_step, end_step))



====================================================

def chars_in_range(start, end):
    global chars
    my_list_with_chars = list()
    for i in range(ord(start) + 1,ord(end)):
        my_list_with_chars.append(chr(i))
        chars = (' '.join(my_list_with_chars))
    return chars


char1 = input()
char2 = input()
print(chars_in_range(char1, char2))

def odd_and_even_sum(text):
    odd_sum = 0
    even_sum = 0
    for ch in text:
        number = int(ch)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num_text = input()
print(odd_and_even_sum(num_text))


===============================================================


#  1000435
def odd_and_even_sum(numberzz):
    odd_numberzz = 0
    even_numberzz = 0

    for num in numberzz:
        if int(num) % 2 == 0:
            even_numberzz += int(num)
        else:
            odd_numberzz += int(num)

    return f"Odd sum = {odd_numberzz}, Even sum = {even_numberzz}"


single_number = input()
print(odd_and_even_sum(single_number))


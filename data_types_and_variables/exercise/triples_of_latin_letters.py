number_of_symbols = int(input())

for first_symbol in range(number_of_symbols):
    for second_symbol in range(number_of_symbols):
        for third_symbol in range(number_of_symbols):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")
=========================================================

n = int(input())

for first_num in range(97, 97 + n):
    for second_num in range(97, 97 + n):
        for third_num in range(97, 97 + n):
            print(f"{chr(first_num)}{chr(second_num)}{chr(third_num)}")

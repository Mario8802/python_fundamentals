def calculation(n):
    counter_result = 1
    for number in range(2, n + 1):
        counter_result *= number

    return counter_result


num = int(input())
num2 = int(input())

first_factorial = calculation(num)
second_factorial = calculation(num2)

result = first_factorial / second_factorial

print(f"{result:.2f}")


#
# import math
#
# number_one = int(input())
# number_two = int(input())
#
# result_one = math.factorial(number_one)
# result_two = math.factorial(number_two)
# final_result = result_one / result_two
# print(f"{final_result:.2f}")


# def calculate_the_factorial(number):
#     for current_number in range(1, number):
#         number *= current_number
#     return number  # initial number factorial -> number!
#
#
# first_number = int(input())
# second_number = int(input())
# first_number_factorial = calculate_the_factorial(first_number)
# second_number_factorial = calculate_the_factorial(second_number)
# result = first_number_factorial / second_number_factorial
# print(f"{result:.2f}")


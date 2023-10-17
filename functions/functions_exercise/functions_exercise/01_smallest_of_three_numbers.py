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
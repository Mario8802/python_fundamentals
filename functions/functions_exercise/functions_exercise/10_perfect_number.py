def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))

================================================


def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
is_perfect_number(number)


def calculator(operation):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero!"

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    elif operation == "multiply":
        return multiply
    elif operation == "divide":
        return divide
    else:
        return "Error: Invalid operation!"

# Using the calculator function to perform different operations
add_function = calculator("add")
print("Result of addition:", add_function(5, 3))

subtract_function = calculator("subtract")
print("Result of subtraction:", subtract_function(10, 4))

multiply_function = calculator("multiply")
print("Result of multiplication:", multiply_function(7, 2))

divide_function = calculator("divide")
print("Result of division:", divide_function(15, 3))

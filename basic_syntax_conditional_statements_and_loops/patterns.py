number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(number - 1, 0, - 1):
    for j in range(0, i):
        print("*", end="")
    print()

def print_inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

# Example usage:
print_inverted_right_triangle(5)


def print_right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

# Example usage:
print_right_triangle(5)


def print_square_pattern(n):
    for i in range(n):
        print("* " * n)

# Example usage:
print_square_pattern(5)

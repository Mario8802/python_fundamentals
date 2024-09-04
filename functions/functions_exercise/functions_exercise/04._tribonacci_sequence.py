def print_tribonacci(n):
    if n == 1:
        print(1)
        return
    elif n == 2:
        print("1 1")
        return
    elif n == 3:
        print("1 1 2")
        return
    
    sequence = [1, 1, 2]
    
    for i in range(3, n):
        next_value = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_value)
    
    print(" ".join(map(str, sequence)))

n = int(input("Enter the number of Tribonacci terms: "))
print_tribonacci(n)

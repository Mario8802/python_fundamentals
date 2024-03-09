number = int(input())

for num in range(number):
    n = int(input())
    if not n % 2 == 0:
        print(f"{n} is odd!")
        exit()
else:
    print("All numbers are even.")

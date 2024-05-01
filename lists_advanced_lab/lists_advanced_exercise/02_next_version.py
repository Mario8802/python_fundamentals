version = [int(digit) for digit in input().split('.')]
version[-1] += 1

for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1
print(".".join(str(number) for number in version))

========================================================================

version = input().split('.')

n1, n2, n3 = int(version[0]), int(version[1]), int(version[2])
n3 += 1

if n3 == 10:
    n3 = 0
    n2 += 1
    if n2 == 10:
        n2 = 0
        n1 += 1

print(f"{n1}.{n2}.{n3}")

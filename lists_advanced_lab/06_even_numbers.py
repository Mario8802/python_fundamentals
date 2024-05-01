numbers = list(map(int, input().split(', ')))
indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(indices)


===============================================================


numbers = [int(x) for x in input().split(', ')]
even_indices = []

for i, num in enumerate(numbers):
    if num % 2 == 0:
        even_indices.append(i)

print(even_indices)

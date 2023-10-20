numbers = list(map(int, input().split(' ')))

average_sum = sum(numbers) / len(numbers)

top_five = [number for number in numbers if number > average_sum]
if len(top_five) == 0:
    print('No')
else:
    print(*sorted(top_five, reverse=True)[:5])
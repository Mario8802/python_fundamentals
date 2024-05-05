data = input().split()

stock = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i + 1])
    stock[food] = quantity

print(stock)

=============================================================

line = input()

elements = line.split(' ')
bakery = {}


for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

print(bakery)

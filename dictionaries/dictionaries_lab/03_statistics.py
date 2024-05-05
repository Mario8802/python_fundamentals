stock = {}

while True:
    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(': ')
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

product_count = len(stock)
total_quantity = sum(stock.values())

print('Products in stock:')


================================================


command = input()
products = {}

while not command == "statistics":
    line = command.split(': ')
    key = line[0]
    value = int(line[1])
    if key not in products:
        products[key] = 0
    products[key] += value
    command = input()


print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

# [print(f"-{key}:{value}") for (key,value) in products]

for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_quantity}')

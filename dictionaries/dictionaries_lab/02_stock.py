products_information = input().split()

stock_data = {}

for i in range(0, len(products_information), 2):
    product = products_information[i]
    quantity = int(products_information[i + 1])
    stock_data[product] = quantity


products_to_search = input().split()

for current_product in products_to_search:
    if current_product in stock_data:
        print(f'We have {stock_data[current_product]} of {current_product} left')
    else:
        print(f'Sorry, we don\'t have {current_product}')



====================================================================



line_with_products = input().split()
searching_products = input().split()

my_products_dict = {}

# Populate the dictionary with product quantities
for i in range(0, len(line_with_products), 2):
    product = line_with_products[i]
    quantity = line_with_products[i + 1]
    my_products_dict[product] = int(quantity)

# Check for each product and print the availability
for product in searching_products:
    if product in my_products_dict:
        print(f"We have {my_products_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

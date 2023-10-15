def calcululate_total_price(product, quantity):
    if product == "coffee":
        return f"{1.50 * quantity:.2f}"
    elif product == "water":
        return f"{1.0 * quantity:.2f}"
    elif product == "coke":
        return f"{1.40 * quantity:.2f}"
    elif product == "snacks":
        return f"{2.0 * quantity:.2f}"

    
product = input()
quantity = int(input())
result = calcululate_total_price(product, quantity)
print(result)
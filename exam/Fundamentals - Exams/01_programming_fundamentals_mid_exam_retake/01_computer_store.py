prices_without_tax = input()

total_price = 0

while prices_without_tax != "special" and prices_without_tax != "regular":
    prices_without_tax = float(prices_without_tax)

    if prices_without_tax < 0:
        print("Invalid price!")

    else:
        total_price += prices_without_tax

    prices_without_tax = input()

if total_price == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    taxes = total_price * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if prices_without_tax == "special":
        discount = (total_price + taxes) * 0.9
        print(f"Total price: {discount:.2f}$")
    else:
        print(f"Total price: {(total_price + taxes):.2f}$")



=========================================================================================================


data = input()
total_sum = 0
taxes = 0

while data != 'special' and data != 'regular':
    try:
        price = float(data)
        if price <= 0:
            print("Invalid price!")
        else:
            total_sum += price
            taxes += price * 0.2
    except ValueError:
        print("Invalid input!")

    data = input()

if total_sum == 0:
    print("Invalid order!")
else:
    total_price = total_sum + taxes
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    
    if data == 'special':
        total_price *= 0.9  # Прилагаме 10% отстъпка
    
    print(f"Total price: {total_price:.2f}$")

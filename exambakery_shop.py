stock_availability = dict()
sold_items = dict()


def receive(quantity, food):
    if quantity <= 0:
        return
    if food not in stock_availability:
        stock_availability[food] = quantity
    else:
        stock_availability[food] += quantity


def sell(quantity, food):
    if food not in stock_availability:
        print(f"You do not have any {food}.")
    else:
        if stock_availability[food] >= quantity:
            stock_availability[food] -= quantity
            sold_items[food] = sold_items.get(food, 0) + quantity
            print(f"You sold {quantity} {food}.")
            if stock_availability[food] == 0:
                del stock_availability[food]
        else:
            sold_items[food] = sold_items.get(food, 0) + stock_availability[food]
            print(f"There aren't enough {food}. You sold the last {stock_availability[food]} of them.")
            del stock_availability[food]


while True:
    command = input().split()
    action = command[0]
    if action == "Complete":
        break
    quantity = int(command[1])
    food = command[2]

    if action == "Receive":
        receive(quantity, food)

    elif action == "Sell":
        sell(quantity, food)


for food, quantity in stock_availability.items():
    print(f"{food}: {quantity}")

total_sold = sum(sold_items.values())
print(f"All sold: {total_sold} goods")

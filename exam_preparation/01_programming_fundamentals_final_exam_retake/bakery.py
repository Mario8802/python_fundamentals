command = input().split()
bakery = {}
sold = {}

while command[0] != "Complete":
    action = command[0]
    quantity = int(command[1])
    food = command[2]

    if quantity <= 0:
        command = input().split()
        continue

    if action == "Receive":
        if food not in bakery:
            bakery[food] = quantity
        else:
            bakery[food] += quantity

    elif action == "Sell":
        if food not in bakery:
            print(f"You do not have any {food}.")
        elif bakery[food] < quantity:
            if food in sold:
                sold[food] += bakery[food]
            else:
                sold[food] = bakery[food]
            print(f"There aren't enough {food}. You sold the last {bakery[food]} of them.")
            bakery.pop(food)
        else:
            if food in sold:
                sold[food] += quantity
            else:
                sold[food] = quantity
            bakery[food] -= quantity
            print(f"You sold {quantity} {food}.")

            if bakery[food] == 0:
                bakery.pop(food)

    command = input().split()

for key, value in bakery.items():
    print(f"{key}: {value}")

total_sold = sum(sold.values())
print(f"All sold: {total_sold} goods")

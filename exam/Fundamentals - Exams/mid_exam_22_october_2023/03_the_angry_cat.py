price = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()

value = price[entry_point]
items_on_the_left = []
items_on_the_right = []
if type_of_items == "cheap":
    for index, item in enumerate(price):
        if item < value and index < entry_point:
            items_on_the_left.append(item)
        elif item < value and index > entry_point:
            items_on_the_right.append(item)
elif type_of_items == "expensive":
    for index, item in enumerate(price):
        if item >= value and index < entry_point:
            items_on_the_left.append(item)
        elif item >= value and index > entry_point:
            items_on_the_right.append(item)

if sum(items_on_the_left) >= sum(items_on_the_right):
    print(f"Left - {sum(items_on_the_left)}")
else:
    print(f"Right - {sum(items_on_the_right)}")
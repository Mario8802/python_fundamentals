# budget = float(input())
# flour_price = float(input())

# eggs_price = flour_price * 0.75
# milk_liter = flour_price * 1.25
# milk_price = milk_liter / 4
# loaf_price = flour_price + eggs_price + milk_price
# colored_eggs = 0
# loaf_count = 0
# while budget >= loaf_price:
#     budget -= loaf_price
#     loaf_count += 1
#     colored_eggs += 3
#     if loaf_count % 3 == 0:
#         colored_eggs -= loaf_count - 2

# budget_left = budget - (loaf_count * loaf_price)
# print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


budget = float(input())
price_for_flour = float(input())
price_for_eggs = price_for_flour * 0.75  # The price for 1 pack of eggs is 75% of the price for 1 kg flour
price_for_milk = price_for_flour * 1.25  # The price for 1L milk is 25% more than the price for 1 kg flour
count_loaf = 0
colored_eggs = 0

while budget:
    loaf_cost = price_for_flour + price_for_eggs + (price_for_milk / 4)
    if budget < loaf_cost:
        break
    budget -= loaf_cost
    count_loaf += 1
    colored_eggs += 3

    if count_loaf % 3 == 0:
        eggs_lost = (count_loaf - 2)
        colored_eggs -= eggs_lost

print(f"You made {count_loaf} loaves of Easter bread!"
      f" Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

# quantity_of_decoration = int(input())
# remaining_days = int(input())
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_lights_price = 15
# total_spirit = 0
# total_cost = 0

# for current_day in range(1, remaining_days + 1):
#     if current_day % 11 == 0:
#         quantity_of_decoration += 2
#     if current_day % 2 == 0:
#         total_cost += quantity_of_decoration * ornament_set_price
#         total_spirit += 5
#     if current_day % 3 == 0:
#         total_cost += quantity_of_decoration * (tree_skirt_price + tree_garland_price)
#         total_spirit += 10 + 3
#     if current_day % 5 == 0:
#         total_cost += quantity_of_decoration * tree_lights_price
#         total_spirit += 17
#         if current_day % 3 == 0:
#             total_spirit += 30
#     if current_day % 10 == 0:
#         total_spirit -= 20
#         total_cost += tree_skirt_price + tree_lights_price + tree_garland_price
# if remaining_days % 10 == 0:
#     total_spirit -= 30

# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")



quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

money_to_spend = 0
points = 0


for day in range(1, days_left_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        money_to_spend += 2 * quantity_of_decorations
        points += 5
    if day % 3 == 0:
        money_to_spend += 8 * quantity_of_decorations
        points += 13
    if day % 5 == 0:
        money_to_spend += 15 * quantity_of_decorations
        points += 17
        if day % 3 == 0:
            points += 30
    if day % 10 == 0:
        points -= 20
        money_to_spend += 23
if days_left_until_christmas % 10 == 0:
    points -= 30


print(f"Total cost: {money_to_spend}")
print(f"Total spirit: {points}")

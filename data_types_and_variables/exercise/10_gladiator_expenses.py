number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // (2 * 3)
total_armor_broken = total_shield_broken // 2
expenses = total_helmet_broken * helmet_price \
            + total_sword_broken * sword_price \
            + total_shield_broken * shield_price\
            + total_armor_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

===============================================================================================================================================


count_lost_fights = int(input())

helmet_cost = float(input())
sword_cost = float(input())
shield_cost = float(input())
armor_cost = float(input())
costs = 0
shield_breaks = 0

for battle in range(1, count_lost_fights + 1):
    if battle % 2 == 0:
        costs += helmet_cost
    if battle % 3 == 0:
        costs += sword_cost
    if battle % 6 ==0:
        costs += shield_cost
        shield_breaks += 1
        if shield_breaks % 2 == 0 and not shield_breaks == 0:
            costs += armor_cost

print(f"Gladiator expenses: {costs:.2f} aureus")

number_of_companions = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_companions -= 2
    if current_day % 15 == 0:
        number_of_companions += 5

    if current_day % 3 == 0:
        coins -= number_of_companions * 3
    if current_day % 5 == 0:
        coins += number_of_companions * 20
        if current_day % 3 == 0:
            coins -= number_of_companions * 2
    coins += 50
    coins -= number_of_companions * 2
coins_per_companions = coins // number_of_companions
print(f"{number_of_companions} companions received {coins_per_companions} coins each.")


import math

companions = int(input())
days = int(input())
coins = 0

for day in range(1,days + 1):
    if day % 15 == 0:
        companions += 5

    if day % 10 == 0:
        companions -= 2

    coins += (50 - 2 * companions)

    if day % 3 == 0:
        coins -= (3 * companions)

    if day % 5 == 0:
        coins += (20 * companions)
         
        if day % 3 == 0:
            coins -= (2 * companions)

total_sum_coins_per_companion = math.floor(coins / companions)

print(f"{companions} companions received {total_sum_coins_per_companion} coins each.")


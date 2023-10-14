number_of_orders = int(input())
total_sum = 0
for order in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    total_price = (days * capsules_needed_per_day) * price_per_capsule
    total_sum += total_price
    if 0.01 < price_per_capsule > 100.00:
        continue
    elif 1 > days > 31:
        continue
    elif 1 > capsules_needed_per_day > 2000:
        continue
        print(f"The price for the coffee is: ${total_price:.2f}")

print(f"Total: ${total_sum:.2f}")
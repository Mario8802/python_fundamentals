number_of_orders = int(input())
total_sum = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        current_order_price = days * capsules_needed_per_day * price_per_capsule
        total_sum += current_order_price
    # if current_order_price == 0:
    #     continue
        print(f"The price for the coffee is: ${current_order_price:.2f}")
    else:
        continue
print(f"Total: ${total_sum:.2f}")

def calculate_discount(price, discount):
    """
    Calculate the price after applying a discount.
    :param price: Original price of the item
    :param discount: Discount percentage
    :return: Discounted price
    """
    discounted_price = price - (price * discount / 100)
    return discounted_price


item_price = 100
discount_percent = 15
final_price = calculate_discount(item_price, discount_percent)
print(f"Final price after discount: ${final_price}")

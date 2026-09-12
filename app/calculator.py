def calculate_discount(price, discount_rate):
    """Calculate the discounted price."""
    return price * (1 - discount_rate)


def calculate_discount_rate(original_price, discounted_price):
    """Calculate the discount rate from two prices."""
    if original_price == 0:
        return 0
    return 1 - (discounted_price / original_price)
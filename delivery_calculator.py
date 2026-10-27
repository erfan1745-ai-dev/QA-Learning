def calculate_order_total(cart_amount):
    if cart_amount < 0:
        raise ValueError("Cart amount cannot be negative")

    if cart_amount < 500000:
        delivery_fee = 30000
    else:
        delivery_fee = 0

    return cart_amount + delivery_fee
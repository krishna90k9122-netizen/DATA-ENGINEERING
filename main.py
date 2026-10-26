def validate_order(order_id, amount, payment_done):
    if order_id <= 0:
        return False

    if amount < 0:
        return False

    if not isinstance(payment_done, bool):
        return False

    return True


order_id = input("Enter order ID: ")
amount = input("Enter order amount: ")
payment_input = input("Payment completed? (yes/no): ").strip().lower()

try:
    order_id = int(order_id)
    amount = float(amount)

    if payment_input not in ("yes", "no"):
        raise ValueError("Payment must be yes or no")

    payment_done = payment_input == "yes"

    if validate_order(order_id, amount, payment_done):
        print("Order is valid")
        print("Order ID:", order_id)
        print("Amount:", amount)
        print("Payment completed:", payment_done)
    else:
        print("Invalid order data")

except ValueError:
    print("Invalid input. Check the ID, amount and payment status.")
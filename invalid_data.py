orders = [
    {"order_id": 101, "customer": " rahul ", "amount": "500", "date": "2026-10-20"},
    {"order_id": 102, "customer": "PRIYA", "amount": "800", "date": "2026-10-21"},
    {"order_id": 103, "customer": " aman ", "amount": "-100", "date": "2026-10-21"},
    {"order_id": 104, "customer": "riya", "amount": "300", "date": "2026-10-22"},
    {"order_id": 105, "customer": " Rahul ", "amount": "500", "date": "2026-10-22"},
    {"order_id": 106, "customer": "", "amount": "250", "date": "2026-10-23"},
    {"order_id": 107, "customer": "Aman", "amount": "invalid", "date": "2026-10-23"},
    {"order_id": 108, "customer": "Neha", "amount": "1900", "date": "2026-10-24"},
]

valid_orders = []
rejected_orders = []


def clean_customer_name(name):
    return name.strip().title()

for order in orders:
    order["customer"] = clean_customer_name(order["customer"])

print("Cleaned Customer Names:")
for order in orders:
    print(f"Order ID: {order['order_id']}, Customer: {order['customer']}, Amount: {order['amount']}, Date: {order['date']}")


for order in orders:
    if order["customer"] == "":
        rejected_orders.append(order)
        continue

    try:
        amount = float(order["amount"])

    except ValueError:

        rejected_orders.append(order)
        continue

    if amount < 0:
        rejected_orders.append(order)
        continue

    order["amount"] = amount
    valid_orders.append(order)

print("\nValid Orders:")
for order in valid_orders:
    print(f"Order ID: {order['order_id']}, Customer: {order['customer']}, Amount: {order['amount']}, Date: {order['date']}")

print("\nRejected Orders:")
for order in rejected_orders:
    print(f"Order ID: {order['order_id']}, Customer: {order['customer']}, Amount: {order['amount']}, Date: {order['date']}")

sum=0 
for order in valid_orders:
    sum=sum+order["amount"]
    
    total_length = len(valid_orders)


print(f"\nTotal Amount of Valid Orders: {sum}")
print(f"average Amount of Valid Orders: {sum / total_length if total_length > 0 else 0}")
print(f"highest Amount of Valid Orders: {max(order['amount'] for order in valid_orders)}")

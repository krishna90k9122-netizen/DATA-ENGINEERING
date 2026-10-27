orders = [
    {"order_id": 101, "amount": 500},
    {"order_id": 102, "amount": 800},
    {"order_id": 103, "amount": -100},
    {"order_id": 104, "amount": 300},
    {"order_id": 105, "amount": -50},
]

total_orders = len(orders)
valid_orders = 0
invalid_orders = 0
total_sales = 0

for index, order in enumerate(orders, start=1):
    order_id = order["order_id"]
    amount = order["amount"]

    if amount < 0:
        invalid_orders += 1
        print(index, order_id, "Invalid order")
        continue

    valid_orders += 1
    total_sales += amount

    print(index, order_id, "Valid order")

print("\n--- SALES SUMMARY ---")
print("Total orders:", total_orders)
print("Valid orders:", valid_orders)
print("Invalid orders:", invalid_orders)
print("Total valid sales:", total_sales)
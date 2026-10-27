customer_id="205"
print(type(customer_id))

customer_id = int(customer_id)
print(type(customer_id))

order_price=249
order_price=int(order_price)

total_price=4*order_price
print(type(total_price))
print(total_price)

age=input("Enter your age: ")
age=int(age)
if age>=18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible to vote.")
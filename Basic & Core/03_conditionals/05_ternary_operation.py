order_amount = int(input("Enter the ordre amount: "))
# Check type of variable
# print(f"Order amount: {type(order_amount)}") 

# If delivery_fees is 0 if the order amount is greater than 300 else order fees will be 30
# e.g. order_amount is 301 then delivery fees = 0 -> else 30
# e.g. order_amount is 200 then delivery fees = 30
delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees is: {delivery_fees}")


# dictionary == objects

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "Milk"
print(f"Chai recipe: {chai_recipe}")
print(f"Chai recipe: {chai_recipe["base"]}")

# Delete
del chai_recipe["liquid"]
print(f"Chai recipe: {chai_recipe}")

# Membership
# Can check key
print(f"Is sugar in order? {'sugar' in chai_order}")


# Keys only
chai_order = dict(type="Ginger Chai", size="Medium", sugar=1)
print(f"Order details keys: {chai_order.keys()}")
print(f"Order details values: {chai_order.values()}")
print(f"Order details Items: {chai_order.items()}")

print(f"Chai Recipe keys: {chai_recipe.keys()}") # dict_keys(['base'])

print(f"\n************************\n\n")

# popitem will remove your last item
last_item = chai_order.popitem()
print(f"Chai order last item: {last_item}")
print(f"Chai order: {chai_order}")

# Update or add new keys to dictionary
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Chai recipe: {chai_recipe}")


print(f"\n************************\n\n")

chai_size = chai_order["size"]
print(f"Chai size: {chai_size}")

# It will crash your application. Because key is not exist.
# chai_customer_note = chai_order["customer_note"]
# Used get method, if key is not exist then default message will show "No customer note"
chai_customer_note = chai_order.get("customer_note", "No customer note")
print(f"Chai size: {chai_customer_note}")



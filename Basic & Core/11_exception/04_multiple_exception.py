def process_order(item, quantity):
    try:
        # Key and value (dictionary). For this dictionary we are looking for an item
        # try to extract the item from dictionary based on the key value which is provided
        # So item will be replace with ginger, e.g. 
        # {"masala":20}["ginger"]
        # Need to convert price and quantity into the number then it will work
        price = {"masala":20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala", "two")


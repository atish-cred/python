ingredients = ["Water", "Milk", "Black Tea"]
ingredients.append("Sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("Sugar")
print(f"Ingredients are: {ingredients}")

spice_options = ["Ginger", "Cardamom"]
chai_ingredients = ["Water", "Milk"]
chai_ingredients.extend(spice_options)
print(f"Chai Ingredients are: {chai_ingredients}")
# Insert will add new value on 2 index
chai_ingredients.insert(2, "Black Tea")
print(f"Chai Ingredients are: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last Added Chai Ingredients is: {last_added}")
print(f"Chai Ingredients are: {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai Ingredients are: {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai Ingredients are: {chai_ingredients}")



sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")





# Operator Overloading

base_liquid = ["Water", "Milk"]
extra_flavor = ["Ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix: {full_liquid_mix}")

strong_brew = ["Black Tea"] * 3
print(f"Strong Brew: {strong_brew}") # ['Black Tea', 'Black Tea', 'Black Tea']

strong_brew = ["Black Tea", "Water"] * 3
print(f"Strong Brew: {strong_brew}") # ['Black Tea', 'Water', 'Black Tea', 'Water', 'Black Tea', 'Water']


from operator import itemgetter

raw_spice_data = bytearray(b"CINNAMON")
print(f"Byte Array: {raw_spice_data}")
raw_spice_data.replace(b"CINN", b"CARD")
print(f"Byte Array: {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD") # If you assign the value to variable the it will work
print(f"Byte Array: {raw_spice_data}")




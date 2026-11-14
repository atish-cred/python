# Integer
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")
print(f"-------------------------\n")


milk_liters = 7
servings = 4
milk_per_serving = milk_liters/servings
print(f"Milk per serving is {milk_per_serving}")
print(f"-------------------------\n")


# After decimal it will not print the value -> e.g. 1.75 to 1 only
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")
print(f"-------------------------\n")


# Remainder
total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover c pods {leftover_pods}")
print(f"-------------------------\n")


# Exponents - 2 the power of 3 = (2x2x2 = 2 power 3)
base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")
print(f"-------------------------\n")


# Readablitity or how to write 1 million
total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves harvested {total_tea_leaves_harvested}")
print(f"-------------------------\n")


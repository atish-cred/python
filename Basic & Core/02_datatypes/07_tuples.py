# Tuples
# If Tuplese are defined you can not change/Add. You need to add into the tuples only
# Can not push the value.

masala_spices = ("Cardamom", "Cloves", "Cinnamon")
# Extract above tuples
(spice1, spice2, spice3) = masala_spices
print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}")


# Ginger = 2, cardamon = 1 --> behind the scene it's used tupes
ginger_ratio, cardamon_ratio = 2, 1
print(f"Ratio: G:{ginger_ratio}, C:{cardamon_ratio}")
# Value also we can switch
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio: G:{ginger_ratio}, C:{cardamon_ratio}")


# Membership --> Checking the string in tuples
print(f"Is ginger in masala spices? {'Ginger' in masala_spices}")
print(f"Is Cinnamon in masala spices? {'Cinnamon' in masala_spices}")




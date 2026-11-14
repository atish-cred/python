essential_spices = {"Cardamom", "Ginger", "Cinnamon"}
optional_spices = {"Cloves", "Ginger", "Black Peper"}


# Union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")


# Intersection
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")


# Unique from essential spices --> remove ginger it common in optional spices
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")


# Membership
print(f"Is 'Cloves' in essential spices? {'Cloves' in optional_spices}")



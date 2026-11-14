# LIST comprehension -->> [expression for item in iterable if condition] 

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

# 1st tea is a variable -->> tea
# then for loop         -->> for tea in menu
# then if condition     -->> if "Iced" in tea
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

# Error will show to my_tea variable,
# because my_tea variable is not comming from for loop and if condition
# iced_tea = [my_tea for tea in menu if "Iced" in tea]

iced_tea = [my_tea for my_tea in menu if len(my_tea) < 12]
print(iced_tea)

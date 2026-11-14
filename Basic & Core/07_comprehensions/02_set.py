# Set comprehension -->> {expression for item in iterable if condition} 
favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

# Unique
# If you use curly {} braces then you don't need to write if conditon
# Automatically unique values will come.
unique_chai = {chai for chai in favourite_chais }
print(unique_chai)

unique_chai = {chai for chai in favourite_chais if len(chai) < 12 }
print(unique_chai)


# Unique values in complex way
recipes = {
    "Masala Chai": ["Ginger", "Cardamom", "Clove"],
    "Elaichi Chai": ["Cardamom", "Milk"],
    "Spicy Chai": ["Ginger", "Black Peper", "Clove"],
}
# recipes.values will be iteration based because we have used in for loop
# e.g
# 1. ["Ginger", "Cardamom", "Clove"]
# 2. ["Cardamom", "Milk"]
# 3. ["Ginger", "Black Peper", "Clove"]
# Not necessary you have to use if condition you can add any conditions -->> like for loop
# unique_spices = { _ for ingredients in recipes.keys()}

# Why ingredient in last for loop? because it is used 1st loop
# 1st variable will be -->> Whatever you are returning from whole code, that will be the variable.    e.g. spice
unique_spices = { spice for ingredients in recipes.values() for spice in ingredients }
print(unique_spices)


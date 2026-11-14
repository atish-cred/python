# Attribute shadowing 

class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

# 
cutting.temperature = "Mild"
cutting.cup = "Small"
print("After changing ", cutting.temperature)
print("Cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

# Attribute shadowing --> If you delete the value which is assigned to object still you will get class attribute value
# Fall back of attribute will work delete --> "Mild" and show "Hot"
del cutting.temperature
del cutting.cup
print(cutting.temperature) # hot

# 
# print(cutting.cup) # Error



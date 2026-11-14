class Chai:
    origin = "India" # variables inside the class, called it properties


print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)


# Creating objects from class chai
masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

# Can manipulate property
masala.is_hot = False
print(f"Class: {Chai.is_hot}")
print(f"Masala: {masala.is_hot}")

# Can add new property
masala.flavor = "Masala"
print(f"Masala: {masala.flavor}")


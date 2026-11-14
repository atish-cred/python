# Method Resolution Order (MRO)
# Multiple inheritance 

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B, C):
    # label = "D: Lemon blend"
    pass

cup = D()
print(cup.label) # "B: Masla blend", because B class is fist inherits.

print(D.__mro__)

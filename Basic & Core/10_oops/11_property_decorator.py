class TeaLeaf:
    def __init__(self, age):
        self._age = age # pythong treat _age as a property e.g. age = _age

    # We define this method as a property
    @property
    def age(self):
        return self._age + 2

    # Using above method we add condition
    @age.setter
    def age(self, age):
        if 1 <= age <= 5: # if age min 1 and max 5
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")


leaf = TeaLeaf(0)
print(leaf.age) # No need to call age function as a leaf.age()

leaf.age = 6 # Age as a property and age is using setter
print(leaf.age)


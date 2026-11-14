class Chaicup:
    size = 150 #ml

    # self is reference of all the properties which is defined in this class
    def describe(self):
        return f"A {self.size}ml chai cup"

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))
# print(Chaicup.describe()) # Error --> No reference is passed


# It is working --> Because it is referencing the self that's why need to pass class name as a reference,
print(Chaicup.describe(Chaicup)) # Work


cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))


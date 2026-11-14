# You are creating a constructor via init Or you can say init creates a constructor
# __init__

class ChaiOrder:
    # type = ""
    # Why type_ used because type as a operator is exists in python
    def __init__(self, type_, size):
        self.type = type_ # it is meaning we are creating type variable with empty value, no need to define above
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"


order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 150)
print(order_two.summary())


# You are creating a constructor via init Or you can say init creates a constructor
# __init__

class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")


# When you inheritance the class that time you have to use () braces.
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger & cloves.")


# Composition
class ChaiShop:
    # Not using () bracket/parentheses because to hold the reference, But also i'll create an object in some time, not immediately
    chai_cls = BaseChai  # BaseChai()

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    # self.chai.type ? self.chai has self.chai_cls and it has type object
    def serve(self):
        print(f"Serving {self.chai.type} chain in the shop")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai



# Calling classes

shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai_cls.add_spices(fancy)

# Composition reference
fancy.chai.add_spices() # Called this method via the class that's why self reference is not required



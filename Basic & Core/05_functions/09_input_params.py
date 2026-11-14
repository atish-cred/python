chai = "Ginger chai"

def prepare_chai(order):
    print("Preparing", order)

prepare_chai(chai)
print(chai)


chai = [1, 2, 3]
def edit_chai(cup): # parameter
    cup[1] = 42

edit_chai(chai) # arguments
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)
make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green tea", sugar="low", milk="yes") # keywords


# * and **  --> it is mixed of positiona and keywords, e.g. above example
# * use for arguments
# ** use for key value arguments  -> kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="Yes")


def chai_order(order=[]):
    order.append("Masala")
    print(order)

# Default traps
chai_order() # ['Masala']
chai_order() # ['Masala', 'Masala']


def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()


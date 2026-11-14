# Built In Functions


def chai_flavor(flavor="Masala"):
    """Return the flavor of chai"""
    chai="Ginger"
    return flavor

# 2 underscore __ called as dunder
# e.g. chai_flavor. ctrl + space
print(chai_flavor.__doc__)  # Document string -->> It should be in first line.
print(chai_flavor.__name__) # Name of function


# Help Function
help(len)


def generate_bill(chai=0, samosa=0):
    """"
    Calculate the total bill for chai and samosa

    :Param chai: Number of chai cups (10 rupees each)
    :Param samosa: Number of samosa (15 rupees each)
    :return: (Total amount, Thank you message)
    """

    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"

print(generate_bill.__doc__)  # Document string -->> It should be in first line.
print(generate_bill.__name__) # Name of function
print(generate_bill())


def make_chai():
    return "Here is your masala chai"
print(make_chai())


print(f"\n ---------------------- \n")

def make_chai():
    # return "Here is your masala chai"
    print("Here is your masala chai")
return_value = make_chai()
print(return_value)


print(f"\n ---------------------- \n")

def idle_chaiwala():
    pass
print(idle_chaiwala())


print(f"\n ---------------------- \n")

def sold_cups():
    return 120
total = sold_cups()
print(total)


print(f"\n ---------------------- \n")

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))


print(f"\n ---------------------- \n")

def chai_report():
    return 100, 20 # sold, remaining
    # return 100, 20, 10 # sold, remaining, Extra
sold, remaining = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)


print(f"\n ---------------------- \n")


def chai_report():
    return 100, 20, 10 # sold, remaining, Extra
sold, remaining, _ = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
print("Remaining _: ", _)


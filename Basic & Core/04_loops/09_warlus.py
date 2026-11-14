# warlus :=
# x=5 is a statement
# 3+3 expression is something which returns a value

value=13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")



# warlus operator :=
value = 13
# remainder := value % 5    #--> It will not work
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")



available_sizes = ["small", "medium", "large"]
if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable {requested_size}")



flavours = ["masala", "ginger", "lemon", "mint"]
print("Available flavors", flavours)

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You choose {flavour} chai")



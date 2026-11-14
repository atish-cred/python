names = ["Atish", "Alex", "Hitesh", "Meera", "Sam"]
bills = [100, 50, 70, 40]

# SAM will not print because index will not match
for name, amount in zip(names, bills):
    print(f"{name} : {amount}")


print(f"\n--------------\n")

names = ["Atish", "Alex", "Hitesh", "Meera",]
bills = [100, 50, 70, 40, 30]

# 30 will not print because index will not match
for name, amount in zip(names, bills):
    print(f"{name} : {amount}")
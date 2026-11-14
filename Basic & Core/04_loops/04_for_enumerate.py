menu = ["Green", "Lemon", "Spiced", "Mint"]

for m in menu:
    print(f"Menu item is {m}")


# 1st is menu
# 2nd is index step
for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")


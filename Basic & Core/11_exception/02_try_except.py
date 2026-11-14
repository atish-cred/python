# KeyError --> Key error

try:
    chai_menu = { "masala": 30, "ginger": 40 }
    chai_menu["elaichi"]
except KeyError:
    print("The key is not present")


print("Hello chai code")

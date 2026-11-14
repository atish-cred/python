chai_type = "Ginger" # Global scope
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # you want to refer something which maybe outside the scop of it.
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()


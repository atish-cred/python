chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type # Global scope
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final global scope", chai_type)

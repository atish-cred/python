# Pure function
def pure_chai(cups):
    return cups * 10

total_chai = 0

# impure functions --> not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


print(f"\n ---------------------- \n")

def pour_chai(n):
    if n ==0: 
        return "All cups poured"
    else:
        print(n, "Poured")
    return pour_chai(n-1)
print(pour_chai(4))


print(f"\n ---------------------- \n")

chai_types = ["light", "Kadak", "Ginger", "Kadak"]

strong_chai = list(filter(pour_chai, chai_types)) # 1st arguments is lambda, 2nd argument is where should i iterate

# Filter the list using chai as a variable and chai type value should be "kadak"
# in lambda you have to name it the iterated value --> e.g. chai = kadak, chai = light ... etc
strong_chai = list(filter(lambda chai: chai=="Kadak", chai_types)) # 1st arguments is lambda, 2nd argument is where should i iterate




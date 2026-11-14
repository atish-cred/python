# 1.
# Name of folder recipes then dot . file name
import recipes.flavors
print(recipes.flavors.elaichi_chai())


# 2. 
# Name of folder recipes then dot . file name -->> from function names
from recipes.flavors import elaichi_chai, ginger_chai
print(elaichi_chai())
print(ginger_chai())


# 3. Relative imports
# Single dot . is used for file is present in same directory
# Double dot .. is used for file present in another directory
# from .recipes.flavors import ginger_chai  -->> Avoid this
# from .recipes.flavors import *            -->> Avoid this
# from recipes.flavors import *             -->> Avoid this
# print(elaichi_chai())


# Dunder init -->> __init__



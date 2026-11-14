# print("Start of pydantic journey")

# import BaseModel for pydantic to work and inherite it.
# create and assign proper input or output types
# To use pydantic you need to create an object first of class
# type annotations -->> are just fields like we have int, string, boolean ... etc
# Model initialization/init  -->> always used unpacked dictionary e.g. **input_data
# Automatic validation will work
# 

from pydantic import BaseModel

class User(BaseModel):
    # below called type annotations --> are just fields like we have int, string, boolean ... etc
    id: int
    name: str
    is_active: bool

# It will give you an pydantic validation error --> is_active = bool
input_data = {'id': 101, 'name': "Chaicode", 'is_active': 23}

# It will work -->> because pydantic always try to convert the value into integer / respective data type.
# input_data = {'id': '101', 'name': "Chaicode", 'is_active': True}


# Why ** because of dictionary/object(JS) we need to spread it.
# Once you create and object/instance of class it will validate automatically
user = User(**input_data)

print(user)


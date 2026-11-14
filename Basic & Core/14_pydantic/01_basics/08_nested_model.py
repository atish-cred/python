from typing import List, Optional
from pydantic import BaseModel

# Model composition -->> The user contains an address model


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address # this address is coming from above class, it is reference of other model


address = Address(
    street='123 Somthing',
    city="Mumbai",
    postal_code="400001"
)

user = User(
    id=1,
    name="Atish",
    address=address,
)


user_data = {
    "id": 1,
    "name": "Atish",
    "address": {
        "street":'123 Somthing',
        "city":"Mumbai",
        "postal_code":"400001"
    },
}

user2 = User(**user_data)
print(user2)


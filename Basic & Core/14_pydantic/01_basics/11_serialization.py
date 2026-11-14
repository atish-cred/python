from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    # Whenever you mark anything as a date time, it will create a problem
    # because date time is not very compatible with any pydantic model
    # That why model_config we need to add configuration for fields

    # If you don't add this or comment out these lines then check the datetime format.
    model_config = ConfigDict(
        # We wanted to overrite datetime using lambda function
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id= 1,
    name= "Atish",
    email= "a@abc.com",
    createdAt=datetime(2026, 3, 15, 14, 30),
    address=Address(
        street="123 Street",
        city="Mumbai",
        postal_code='400001'
    ),
    is_active=False,
    tags=["Premium", "Subscriber"]
)

# There is special method to use this
python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)

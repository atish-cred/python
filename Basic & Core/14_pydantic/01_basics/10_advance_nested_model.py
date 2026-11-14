from pydantic import BaseModel
from typing import Optional, List, Union


# ------------------------------------
# Optional Nested Models
# ------------------------------------

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None




# ------------------------------------
# Mixed Data Type
# 
# Different Examples -->> Union
# ------------------------------------

class TextContent(BaseModel):
    type: str = "Text"
    content: str 

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

# Union can be TEXT OR IMAGE
class Article(BaseModel):
    title: str
    section: List[Union[TextContent, ImageContent]]



# ------------------------------------
# Deeply Nested Structure
# ------------------------------------

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = [] # Empty List assigned


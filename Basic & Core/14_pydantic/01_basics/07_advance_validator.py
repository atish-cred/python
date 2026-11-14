from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


class Person(BaseModel):
    first_name: str
    last_name: str

    # Below validation will work on both field one by one
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, value):
        if not value.istitle():
            raise ValueError("Names must be capitalized")
        return value


class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, value):
        return value.lower().strip()


class Product(BaseModel):
    price: str # $4,44 or $4.44

    # field validator also have modes 
    @field_validator('price', mode="before")
    def parse_price(cls, value):
        if isinstance(value.price, str):
            return float(value.replace('$','').replace(",",""))
        return value


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError("end_date must be after start date")
        return values



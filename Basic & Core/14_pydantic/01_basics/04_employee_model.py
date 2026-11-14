from typing import Optional
from pydantic import BaseModel, Field
import re # re is regular expression

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # ... it is indicate as a required field
        min_length=3,
        max_length=50,
        description="Employee name",
        examples="Atish Pawar"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000, # greater than or equal to >=
        le=50000, # less than or equal to <=
        # gt=10000, # greater than >
        # lt=30000, # less than <
        # regex="" # regex validation
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r"" # regular expression
    )
    phone: str = Field(
        ...,
        regex=r''
    )
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage",
    )



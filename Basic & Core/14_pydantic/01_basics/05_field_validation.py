from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    userName: str

    @field_validator('userName')
    def username_length(cls, v): # class reference is required for this decorator
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    

class SingupData(BaseModel):
    password: str
    confirm_password: str

    # In model validator you need to provide modes
    # model validator it will run after the field validation
    # model validator access all the values at same time
    @model_validator(mode='after') 
    def password_match(cls, values): 
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values





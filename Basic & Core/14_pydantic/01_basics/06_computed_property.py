from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    quantity: int

    # In Computed field decorator we can use another decorator
    # Why need to use computed field? Because some computed values can calculate on runtime or by pydantic
    # computed field decorator marks the field as computed, that means it will be calculated on the go.
    # And calculated value can be accessible in property decorator as an attribute. That's why need to use property decorator
    @computed_field
    @property
    def total_price(self) -> float: # here float is return value
        return self.price * self.quantity


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=100.0,
)

# Total amount will became property
print(booking.total_amount)

# Model dump will give you whole model dump --> it means what is inside the class.
print(booking.model_dump())

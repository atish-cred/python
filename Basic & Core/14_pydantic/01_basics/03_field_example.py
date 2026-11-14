from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str] # List -->> array (mutable - can change) --> inside list we have define we need string e.g. typescript
    quantities: Dict[str, int] # Dict(Dictionary) -->> Objects (JS) --> first will be a key and second will be value, both type are defined here


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None # We have use Optional here because we are not sure we get this or not and default value is set


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"Laptop": 1, "Mouse": 2, "Keyboard": 3}
}

cart = Cart(**cart_data)

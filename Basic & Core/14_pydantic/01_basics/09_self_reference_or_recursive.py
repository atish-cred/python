from typing import List, Optional
from pydantic import BaseModel

# Replies are optional but if replies are provided then it should be a LIST['Comment'] -->> Means it should be a comment it's self Comment class
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

# Whenever you are trying for self referencing build the model
# It is forward references -->> In the forward references use quote '' in the model name
# then model rebuild, it is required after self referencing model
Comment.model_rebuild()

comment = Comment(
    id= 1,
    content="First comment",
    replies=[
        Comment(id=2, content= "Reply 1"),
        Comment(id=3, content= "Reply 2"),
        # Nested -->> nested
        Comment(id=4, content= "Reply 3", replies=[
            Comment(id=5, content= "Reply 4"),
        ]),
    ]
)


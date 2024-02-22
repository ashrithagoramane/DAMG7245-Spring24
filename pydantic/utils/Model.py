from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = 'Jane Doe'
    age: int = Field(gt=0)

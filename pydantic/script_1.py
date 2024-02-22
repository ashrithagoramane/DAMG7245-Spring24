from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

user = User(id='123')
assert user.id == 123
assert isinstance(user.id, int)
# Note that '123' was coerced to an int and its value is 123


assert user.name == 'Jane Doe'

from dataclasses import dataclass

@dataclass
class DataclassAuthor:
    firstname: str
    middlename: str
    surname: str

from pydantic import BaseModel, Field

class Author(BaseModel):
    firstname: str = Field(min_length=3, max_length=10, pattern=r"[A-Z]")
    middlename: str
    surname: str
    age: int = Field(gt=0)

turing_author = DataclassAuthor(firstname='Alan', middlename='M', surname='Turing')
print(f"{turing_author.firstname} {turing_author.surname} authored many influential publications in computer science.")
    
turing_author = Author(firstname='Alan', middlename='M', surname='Turing', age=-32)
print(f"{turing_author.firstname} {turing_author.surname} authored many influential publications in computer science.")

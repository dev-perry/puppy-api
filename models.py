from pydantic import BaseModel

class Puppy(BaseModel):
    name: str
    breed: str
    age: int
    color: str
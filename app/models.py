from typing import Union
from pydantic import BaseModel, EmailStr


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    username: str
    password: str
    email: EmailStr

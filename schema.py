from pydantic import BaseModel
from enum import Enum


class Item(BaseModel):
    name: str
    price: float
    
    class Config:
        schema_extra = {"example": {"name": "pizza", "price": 10.99}}

class Order(BaseModel):
    items: list[int] # list of item ids
    
    class Config:
        schema_extra = {"example": {"items": [0, 1, 2]}}
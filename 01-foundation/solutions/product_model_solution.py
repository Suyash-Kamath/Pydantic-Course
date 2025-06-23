from pydantic import BaseModel

# TODO : Create a product model with id,name,price,in_stock

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True # default value daal saktey hai


from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore

# but dont we have controllers for that ?

class User(BaseModel):
    username: str
    # pehele run hotey hai pydantic ke jaane se pehele , mode is automatially before
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    # custom validation ke baad merepaas aao , iss decorator ke paas 
    @model_validator(mode='after')
    # class, values in bracket
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

    # naya property banake aap easily access karke validation bhi kar saktey ho 
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    # full name banana hai toh first name and last name lelo , aise bhi property ban sakti hai
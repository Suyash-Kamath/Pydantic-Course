from pydantic import BaseModel , EmailStr
from fastapi import FastAPI, Depends

# How pydantic models converted into dependency injection

app  = FastAPI()


class UserSignUp(BaseModel):
    username:str
    email:EmailStr
    password:str


class Settings(BaseModel):
    app_name:str= "Chai App"
    admin_email: str = 'admin@sk.com'


# I want to use class Setting as dependency injection

def get_settings():
    return Settings()

@app.post('/signup')
def signup(user:UserSignUp):
    return {'message':f'User {user.username} signed up successfully'}

@app.get('/settings')
def get_settings_endpoint(settings:Settings = Depends(get_settings)):
    return settings
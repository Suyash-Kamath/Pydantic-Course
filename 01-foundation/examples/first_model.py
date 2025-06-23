from pydantic import BaseModel
# So whenever you make classes or objects of Pydantic , you inherit BaselModel 


class User(BaseModel):
    id:int
    name:str
    is_active:bool

input_data = {
    'id':101,
    'name':"ChaiCode",
    'is_active':'True'
}
# Pydantic converts the datatype , it tries to convert the datatype , pydantic converted 'True' , but not all , okayy
# it converts whatever it tries to convert , it saves from possible error
# there is no runtime error by pydantic , only compile time error

user = User(**input_data)

print(user)




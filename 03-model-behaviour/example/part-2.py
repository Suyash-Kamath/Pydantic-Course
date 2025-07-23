from pydantic import BaseModel, model_validator

class User(BaseModel):
    name: str

    @model_validator(mode="before")
    @classmethod
    def strip_name(cls, data):
        # Ensure 'name' exists and is a string
        if 'name' in data and isinstance(data['name'], str):
            data['name'] = data['name'].strip().title()  # Trim and title-case the name
        return data

# Create a user with extra spaces
user = User(name="   suyash kamath   ")

# Print the result
print(user)
print(user.model_dump())  # as dictionary
print(user.model_dump_json())  # as JSON string

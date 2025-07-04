from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime  # datetime field
    address: Address
    tags: List[str] = []

    # ✅ Add model_config INSIDE the class
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

# ✅ Create instance
user = User(
    id=1,
    name="Suyash",
    email="suyash@sk.com",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Something",
        city="Mumbai",
        zip_code="001144"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

# ✅ Pydantic role in serialization

# Convert to Python dict
python_dict = user.model_dump()
print("Python dict:", python_dict)
print("=================================================================\n")
# Convert to JSON string (custom datetime format will apply here)
json_str = user.model_dump_json()
print("JSON string:", json_str)

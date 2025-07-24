from pydantic import BaseModel
from typing import List, ForwardRef

# Forward reference for type hint
Pet = ForwardRef('Pet')

class Owner(BaseModel):
    name: str
    pets: List[Pet]  # Referencing Pet before it's defined

class Pet(BaseModel):
    name: str
    species: str

# Resolving forward references
Owner.model_rebuild()

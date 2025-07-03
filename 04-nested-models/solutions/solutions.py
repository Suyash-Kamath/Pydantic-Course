from pydantic import BaseModel #type: ignore
from typing import List

# TODO : Create Course Model
# Each Course has Modules
# Each Modules has lessons

class Lesson(BaseModel):
    lesson_id:id
    topic:str

class Module(BaseModel):
    module_id:int
    name:str
    lessons:List[Lesson]

class Course(BaseModel):
    course_id:int
    title:str
    modules:List[Module]

# Note : No need to using model_rebuild() , because we are not self referencing , and resolving forward referencing
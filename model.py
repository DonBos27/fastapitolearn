from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

class Gender (str, Enum):
    male = "male"
    female = "female"

class Roles (str, Enum):
    admin = "admin"
    lecturer = "lecturer"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    name: Optional[str]
    gender: Gender
    roles: List[Roles]
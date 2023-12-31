from fastapi import FastAPI
from typing import List
from uuid import uuid4,UUID
from model import User, Gender, Roles

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("f395cc92-09dc-4efc-af24-c2940e923b04"),
        first_name="Donatelo",
        last_name="Buka",
        name="Bosenga",
        gender= Gender.male,
        roles = [Roles.student]
    ),
        User(
        id=UUID("0c03bc95-5bf9-48a8-a62c-93e465676667"),
        first_name="Johnito",
        last_name="Tshilumba",
        name="Muninga",
        gender= Gender.male,
        roles = [Roles.lecturer, Roles.admin]
    )
]

@app.get("/")
def root():
    return {"Hello : World"} 

@app.get("/api/v1/users")
async def root():
    return db,
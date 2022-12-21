from typing import Optional, List
from fastapi import FastAPI
from uuid import uuid4, UUID
#models is the file that we created and we import the classes in this program
from models import User, Gender, Role

#create and instance of application
app = FastAPI()

#create a list of users and add couple of users
db: List[User] = [
    User(
     id=uuid4(),
     first_name="Tejas",
     last_name="Takalkar",
     gender = Gender.male,
     roles = [Role.student]
    ),

    User(
     id=uuid4(),
     first_name="Alexa",
     last_name="Jones",
     gender = Gender.female,
     roles = [Role.admin, Role.user]
    )    
]
#This will give a route for a get request, "/" :- indicates root
@app.get("/")

#define the method called root
def root():
    #return this dictionary
    return{"Hello": "Tejas"}
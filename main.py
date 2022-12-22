from typing import Optional, List
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
#models is the file that we created and we import the classes in this program
from models import User, Gender, Role

#create and instance of application
app = FastAPI()

#create a list of users and add couple of users
db: List[User] = [
    User(
     #this will generate a random uuid everytime we refresh the browser
     id=uuid4(),
     first_name="Tejas",
     last_name="Takalkar",
     gender = Gender.male,
     roles = [Role.student]
    ),

    User(
    # We copy the uuid from browser and paste here to avoid different uuid everytime
     id=UUID("bdb50b2d-c4da-4e67-a7bf-eeedc7f9eaa0"),
     first_name="Alexa",
     last_name="Jones",
     gender = Gender.female,
     roles = [Role.admin, Role.user]
    )    
]
#This will give a route for a get request, "/" :- indicates we will see the data at localhost:8000/ i.e root
@app.get("/")
#define the method called root
async def root():
    #return this dictionary
    return{"Hello": "Tejas"}

# the path indicates we will see the data at localhost:8000/users 
@app.get("/users")
async def fetch_users():
    return db

# this method will be at same path as get
@app.post("/users")
async def register_user(user: User):
    # we register new user in database
    db.append(user)
    #we send him id
    return{"id": user.id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    # if the condition above is satisfied the 'return' statements exits the function else we raise an exeception
    raise HTTPException(
        status_code=404,
        detail =f"user with id: {user_id} does not exist"
    )
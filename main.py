from fastapi import FastAPI

#create and instance of application
app = FastAPI()

#This will give a route for a get request, "/" :- indicates root
@app.get("/")

#define the method called root
def root():
    #return this dictionary
    return{"Hello": "World"}
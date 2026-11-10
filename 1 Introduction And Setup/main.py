# To run this, we type uvicorn filename:object_name --reload
# uvicorn: It's a server in top of which our fastapi works.
# reload: when in future we change our code, we would not have to refresh it again and again
# Importing Our Framework. Here FastAPI is a class
from fastapi import FastAPI

# Here app is the object FastAPI
app = FastAPI()

@app.get('/')
def greet():
    return {"Hello And Nice To Meet You!"}
# Importing Our Framework. Here FastAPI is a class
From fastapi import FastAPI

# Here app is the object FastAPI
app = FastAPI()

@app.get('/')
def greet():
    return {"Hello And Nice To Meet You!"}
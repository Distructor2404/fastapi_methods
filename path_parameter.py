from fastapi import FastAPI

app = FastAPI()

@app.get("/animal/{animal_name}") 
async def get_animal(animal_name: str):
    return {"animal_id": animal_name } #accept only string

@app.get("/user/me")
async def read_user_me():
    return {"user_id": "the current user"} #accept any value

@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id} #accepts only integer
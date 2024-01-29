from fastapi import FastAPI
from enum import Enum
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



class Color(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"
    yellow = "yellow"

@app.get("/color/{color}")
async def read_color(color: Color):
    if color is Color.red:
        return {"color": color,"message": "The color is red"}
    
    if color is Color.green:
        return {"color": color,"message": "The color is green"}
    
    if color is Color.blue:
        return {"color": color,"message": "The color is blue"}  
    
    if color is Color.yellow:
        return {"color": color,"message": "The color is yellow"}

    return {"color": color,"message": "The color is not found"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
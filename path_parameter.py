from fastapi import FastAPI

app = FastAPI()

@app.get("/animal/{animal_name}") 
async def get_animal(animal_name: str):
    return {"animal_id": animal_name } 



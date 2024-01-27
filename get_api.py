from fastapi import FastAPI
app = FastAPI()
import uvicorn

@app.get("/items/")
def read_items():
    return [{"First name": "Abhishek Kumar"}, {"Last name": "Singh"}]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
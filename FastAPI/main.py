from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

# Path operation decorators
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# Path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Query parameters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# Path parameters with type conversion
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Multiple path operations with the same path and same HTTP methods
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# Path parameters with Enum
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

# Path parameters with path converter
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}




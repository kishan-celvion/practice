from random import random
from fastapi import FastAPI, Query # type: ignore
from enum import Enum
from pydantic import BaseModel # type: ignore
from typing import Annotated
from pydantic import AfterValidator # type: ignore

# Enum class for model names
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# Pydantic model for items
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# Path operation decorators
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# Path parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# Query parameters
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# Path parameters with type conversion
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# Multiple path operations with the same path and same HTTP methods
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]
# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]

# Path parameters with Enum
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}

# Path parameters with path converter
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}





# Query parameters with default values
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# Query parameters with default values and type conversion
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# Multiple path parameters and query parameters
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# Required query parameters --> here, needy 
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

# Required query parameters with type conversion and default values
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# Enum values as query parameters
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, model_name: ModelName):
#     item = {"item_id": item_id, "model_name": model_name}
#     if model_name == ModelName.alexnet:
#         item.update({"message": "Deep Learning FTW!"})
#     elif model_name.value == "lenet":
#         item.update({"message": "LeCNN all the images"})
#     else:
#         item.update({"message": "Have some residuals"})
#     return item 





# Request Body
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# Request Body with path parameters
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}

# Request Body with path parameters and query parameters
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result





# Query parameters and string validations (QPnSV)
@app.get("/items/")
async def read_items(q: str | None = None):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

# QPnSV like min_length, max_length, and pattern with Query and Annotated 
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

# QPnSV with Query and default values
@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# QPnSV with Query and type conversion without default values
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# QPnSV with Query and type conversion without default values
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# QPnSV with Query and type conversion without default values and with None as default value
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# QPnSV with Query and type conversion without default values and with None as default value and with list of strings
@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

# QPnSV with Query and type conversion without default values and with None as default value and with list of strings without None as default value
@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
# async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items

# Declare more metadata for query parameters
@app.get("/items/")
async def read_items(
    q: Annotated[str | None, 
                 Query(title="Query string", description="Query string for the items to search in the database that have a good match", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Alias parameters --> http://127.0.0.1:8000/items/?item-query=foobaritems
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Deprecating parameters --> http://127.0.0.1:8000/docs#/default/read_items_items__get
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Exclude parameters from OpenAPI --> http://127.0.0.1:8000/items/?hidden_query=foobaritems
@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
    
# Custom Validation
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
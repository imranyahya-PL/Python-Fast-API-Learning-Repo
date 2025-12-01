# from fastapi import FastAPI, Header
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}


# # name as part of URL
# @app.get("/greetName/{name}")
# async def greet(name: str) -> dict:
#     return {"message": f"Hello, {name}!"}


# # name as query param
# @app.get("/greet")
# async def greet(name: str) -> dict:
#     return {"message": f"Hello, {name}!"}


# # name as part of URL and age as query param
# @app.get("/greet/{name}")
# async def greet(name: str, age: int) -> dict:
#     return {"message": f"Hello, {name}!", "Age": f"You are {age} years old."}


# # name as option and age as query param
# @app.get("/greetOptional")
# async def greet(name: Optional[str] = "Imran",
#                 age: int = 35) -> dict:
#     return {"message": f"Hello, {name}!", "Age": f"You are {age} years old."}


# class BookCreateModel(BaseModel):
#     title: str
#     author: str

# # name as option and age as query param


# @app.post("/create_book")
# async def create_book(book_data: BookCreateModel) -> dict:
#     return {"title": book_data.title,
#             "author": book_data.author}


# # get headers from request
# # Note: status_code=200 is default for GET requests
# @app.get("/get_headers")
# async def get_headers(
#     accept: str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     request_headers = {
#         "accept": accept,
#         "content_type": content_type,
#         "user_agent": user_agent,
#         "host": host}
#     return request_headers

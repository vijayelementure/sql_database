from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()       # instance of a class FastAPI()

@app.get('/')
def index():
    return {"data":"blog list"}


@app.get('/blog/unpublished')
def unpublished():
    return {"data":"all unpublished blogs"}


@app.get('/blog/vijay')
def show(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {"data":f"{limit} published blogs from the list"}
    else:
        return {"data":f"{limit} blogs from the db"}


@app.get('/blog/{id}/comments')
def comments(id):
    return {"data":{"1","2"}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {"data": f"blog is created with as {request.title}"}
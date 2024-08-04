from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'Shrikant'}}

@app.get('/num/{id}')
def check(id:int):
    return {'data':id}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog')
def index(limit=10,num=16,published:bool=True,sort:Optional[str]=None):
    return {'data':f'{limit}-{num}-{published}'}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def createBlog(blog:Blog):
    return 'Blog is created'
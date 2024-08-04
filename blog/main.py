from fastapi import FastAPI
from .database import engine,Base
from .routers import blogs,user


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(blogs.router)
app.include_router(user.router)
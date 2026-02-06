from fastapi import FastAPI
from app.models import Post
from app.database import engine, Base
from app import routers

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.router)

@app.get("/")
def root():
    return {"message": "Hello World!"}
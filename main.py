from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base,engine


Base.metadata.create_all(engine)
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def index():
    return {"message":"Cab booking system api"}
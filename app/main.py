from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base,engine
import os


Base.metadata.create_all(engine)
app=FastAPI()
port = int(os.environ.get("PORT","8000"))
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


#Starting the fastapi app only when the app is called directly
if "__name__"=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=port)
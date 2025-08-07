from pydantic import BaseModel
from typing import Optional

class UserSignIn(BaseModel):
    fullName:str
    email:str
    password:str
    gender:str
    phone_number:str
    address:str
    profile_picture:Optional[str]


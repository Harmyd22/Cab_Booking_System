from .database import Base
from sqlalchemy import Column,String,ForeignKey,Integer
from sqlalchemy.orm import Relationship



class User(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,index=True)
    fullname=Column(String,index=True)
    email=Column(String,index=True,unique=True)
    password=Column(String)
    gender=Column(String)
    phone_number=Column(String,unique=True)
    address=Column(String)
    role=Column(String,default="User")
    profile_picture=Column(String,nullable=True)
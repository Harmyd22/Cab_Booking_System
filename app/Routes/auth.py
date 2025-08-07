from fastapi import status,Form,File,UploadFile,APIRouter,Depends
from typing import Optional
from ..database import Session,get_db
from ..Services.auth import Signup,log_in
from ..schema import Login



auth=APIRouter(prefix="/auth")
@auth.post("/signup",status_code=status.HTTP_200_OK)
def signup(
    fullName:str=Form(...),
    Email:str=Form(...),
    Password:str=Form(...),
    Gender:str=Form(...),
    Phone_number:str=Form(...),
    Address:str=Form(...),
    Profile_picture:Optional[UploadFile]=File(default=None),
    db:Session=Depends(get_db)
):
    return Signup(fullName,Email,Password,Gender,Phone_number,Address,Profile_picture,db)

@auth.post("/login",status_code=status.HTTP_202_ACCEPTED)
def login(request:Login,db:Session=Depends(get_db)):
    return log_in(request,db)
    

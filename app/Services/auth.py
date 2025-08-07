from fastapi import UploadFile,status
import cloudinary
from ..models import User
from fastapi.responses import JSONResponse
from ..Utils.validator import valid_email,validate_password
from ..Utils.hash import Hash
from ..database import Session
from ..Utils.Token import create_access_token


def Signup(FullName,Email,Password,Gender,Phone_number,Address,Profile_picture:UploadFile,db:Session):
    Fullname=FullName.strip().lower()
    Email_validation=valid_email(Email.strip().lower())
    if isinstance(Email_validation,JSONResponse):
        return Email_validation
    email=Email_validation
    #checking if the email exists already
    existing_email=db.query(User).filter(User.email==email).first()
    if existing_email:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message":"Email exists"}
        )
    #checking if the phone number exists
    existing_phone_number=db.query(User).filter(User.phone_number==Phone_number).first()
    if existing_phone_number:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message":"Phone number exists"}
        )
    #check if the password match all requirement and hash the password
    password_validation=validate_password(Password)
    if isinstance(password_validation,JSONResponse):
        return password_validation
    Password=password_validation
    try:
        url=None
        if Profile_picture:
            result=cloudinary.uploader.upload(
                Profile_picture.file,
                folder="User_image",
                resource_type="image"
            )
            url=result["secure_url"]
        new_user=User(fullname=Fullname,email=Email,password=Password,gender=Gender,phone_number=Phone_number,address=Address,profile_picture=url)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message":"Signed up Successfully",
                "access_token":create_access_token(
                                    data={
                                        "user_id":new_user.id,
                                        "email":new_user.email}
                                        ),
                "Token_type":"Bearer",
                }
        )
    except Exception as e:
        db.rollback()
        return JSONResponse(
            content={"message":str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    

#LOGIN

def log_in(request,db:Session):
    EmailValid=valid_email(request.email.strip().lower())
    if isinstance(EmailValid,JSONResponse):
        return EmailValid
    Email=EmailValid
    #check if the email is in db
    user=db.query(User).filter(User.email==Email).first()
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message":"Email does not exist"}
        )
    Hasher=Hash()
    #check if password match with the one in db(returns boolean)
    password_validity=Hasher.verify_hash(request.password,user.password)
    if password_validity==False:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message":"Wrong Password"}
        )
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
                 "message":"LoggedIn Successfully",
                 "access_token":create_access_token(
                     data={
                         "user_id":user.id,
                         "email":user.email
                         }
                     ),
                 "Token_type":"Bearer"
                 }
                 
    )
    
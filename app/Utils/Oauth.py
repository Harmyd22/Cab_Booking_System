from fastapi.security import OAuth2PasswordBearer
from fastapi import status,Depends
from jose import jwt,JWTError
from fastapi.responses import JSONResponse
from .config import Secret_key,Algorithm

password_bearer=OAuth2PasswordBearer("/login")

def verify_token(token:str=Depends(password_bearer)):
    try:
        data=jwt.decode(token,Secret_key,algorithms=Algorithm)
        user_id=data.get("user_id")
        email=data.get("email")
        if not user_id or not email:
            return JSONResponse(
                content={"message":"Invalid token payload"},
                status_code=status.HTTP_404_NOT_FOUND
            )
        return {"user_id":user_id,"email":email}
    except JWTError as e:
        return JSONResponse(
            content={"message":str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        


    

    


from jose import jwt,JWTError
from datetime import datetime,timedelta
from typing import Optional
from .config import Secret_key,Algorithm

def create_access_token(data:dict,expiry:Optional[timedelta]=None):
    to_encode=data.copy()
    if(expiry):
        expiry=datetime.utcnow()+expiry
    else:
        expiry=datetime.utcnow()+timedelta(hours=3)
    to_encode.update({"exp":expiry})
    encoded_jwt=jwt.encode(to_encode,Secret_key,algorithm=Algorithm)
    return encoded_jwt


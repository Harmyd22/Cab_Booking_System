from passlib.context import CryptContext

password_context=CryptContext(schemes=['bcrypt'],deprecated="auto")

class hash():
    def hash_password(self,password):
        return password_context.hash(password)
    def verify_hash(self,hashed_password,plain_password):
        return password_context.verify(plain_password,hashed_password)
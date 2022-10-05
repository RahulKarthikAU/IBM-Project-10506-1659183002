import bcrypt
import jwt
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def hash_password(user_password):
    encoded_pw = user_password.encode('utf-8')
    salt = bcrypt.gensalt();
    hash = bcrypt.hashpw(encoded_pw, salt)
    return hash

def compare_hash(user_password, hash):
    encoded_pw = user_password.encode('utf-8')
    encoded_hash = hash.encode('utf-8')
    result = bcrypt.checkpw(encoded_pw, encoded_hash)
    print(result)
    return result

def create_jwt_token(data):
    token = jwt.encode(data, getenv('JWT_SECRET_KEY'), algorithm="HS256")
    return token

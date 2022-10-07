import bcrypt
import jwt
from dotenv import load_dotenv
from os import getenv
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from ..config.mail_config import get_mail

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

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(getenv('JWT_SECRET_KEY'))
    return serializer.dumps(email, salt=getenv('PASSWORD_SALT'))


def confirm_token(token, expiration=900):
    serializer = URLSafeTimedSerializer(getenv('JWT_SECRET_KEY'))
    try:
        email = serializer.loads(
            token,
            salt=getenv('PASSWORD_SALT'),
            max_age=expiration
        )
    except:
        return False
    return email

def send_confirmation_token(email):
    token = generate_confirmation_token(email)    
    mail = get_mail()

    confirm_url =f"http://localhost:5500/confirm.html?token={token}"
    confirm_html = f"<p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p><p><a href={confirm_url}>{confirm_url}</a></p><br><h4>Happy Spending</h4>"

    msg = Message(subject="Confirm E-Mail from Spency", sender=getenv("MAIL_USERNAME"), recipients=[email], html=confirm_html)
    mail.send(msg)
    return True
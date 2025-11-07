from app.models.User import User 
from app import db,bcrypt

# from werkzeug.security import generate_password_hash

def register_user(first_name,last_name,email,password):
    if User.query.filter_by(email=email).first():
        return None,'Email Already Exists !'
    
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(first_name=first_name,last_name=last_name,email=email,password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user,None 

def authenticate_user(email,password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password,password):
        return user 
    return None
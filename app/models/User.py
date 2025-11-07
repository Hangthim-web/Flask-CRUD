from app import db 
from datetime import datetime 

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False,unique=True)

    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupate=datetime.utcnow)
    deleted_at = db.Column(db.DateTine,nullable=True,index=True)


    def __repr__(self):
        return f'<user {self.email}>'
    
    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
        db.session.commit()


    def restore(self):
        self.deleted_at = None 
        db.session.commit()

    @property 
    def is_deleted(self):
        return self.deleted_at is not None
from app import db 
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    description = db.Column(db.String(500),nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self):
        return f'<User {self.title}>'
    
    def soft_delete(self):
        self.deleted_at = datetime.utcnow
        db.session.commit()
    
    def restore(self):
        self.deleted_at = None 
        db.session.commit()
    @property 
    def is_deleted(self):
        return self.deleted_at is not None
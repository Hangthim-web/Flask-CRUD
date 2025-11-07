from app import db 
from app.models.Blog import Blog

def create_blog(title,description):
    blog = Blog(title=title,description=description)
    db.session.add(blog)
    db.session.commit()
    return blog 

def get_blog_by_id(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return blog 

def get_all_blogs():
    blogs = Blog.query.all()
    return blogs 

def update_blog(blog_id,title,description):
    blog = get_blog_by_id(blog_id)
    blog.title = title 
    blog.description = description
    db.session.commit()
    return blog 

def delete_blog(blog_id):
    blog = get_blog_by_id(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return True      

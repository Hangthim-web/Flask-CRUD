from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.models.Blog import Blog 
from app import db 
from app.services.blog_services import create_blog,delete_blog,get_all_blogs,get_blog_by_id,update_blog

blogs_bp = Blueprint('blogs',__name__)

@blogs_bp.route('/create-blogs',methods=["GET","POST"])
def create():
    if request.method == "POST":
        create_blog(
            request.form.get("title"),
            request.form.get("description")
        )
        flash("Blog Created",'success')
        return redirect(url_for('blogs.list_all_blogs__'))
    return render_template('blog/create.html')

@blogs_bp.route('/blogs')
def list_all_blogs__():
    blog_lists = get_all_blogs()
    return render_template('blog/list.html',blogs=blog_lists)


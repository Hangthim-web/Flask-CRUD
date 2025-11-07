from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_migrate import Migrate


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:thistimeforsure@localhost/flask_crud'
    app.config['SQLALCHEMY_FLASK_MODIFICATION']  = False 


    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)

    return app
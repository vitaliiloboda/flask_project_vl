from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_project_vl.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    print(__name__)
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(Config)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from flask_project_vl.main.routes import main
    from flask_project_vl.users.routes import users
    from flask_project_vl.posts.routes import posts
    from flask_project_vl.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app

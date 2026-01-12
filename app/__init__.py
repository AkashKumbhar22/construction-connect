from flask import Flask
from .config import Config
from .extensions import db, login_manager
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # ✅ THIS FIXES YOUR ERROR
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.auth import auth
    from .routes.worker import worker
    from .routes.search import search

    app.register_blueprint(auth)
    app.register_blueprint(worker)
    app.register_blueprint(search)

    with app.app_context():
        db.create_all()

    return app

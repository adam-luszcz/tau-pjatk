from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Xo6h3HsJqPx40vkoBThH22hxy3u3jFDtm4UUHI39'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    @app.before_request
    def before_request():
        db.engine.raw_connection().execute('PRAGMA foreign_keys=ON;')

    from .views import views
    from .auth import auth
    from .topic import topic
    from .thread import thread
    from .post import post

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(topic, url_prefix='/api/')
    app.register_blueprint(thread, url_prefix='/api/')
    app.register_blueprint(post, url_prefix='/api/')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', user=current_user), 404

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

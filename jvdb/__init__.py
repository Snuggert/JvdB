from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flaskext.markdown import Markdown
import os


# Startup stuff
app = Flask(__name__)
app.config.from_object('config')
Markdown(app)

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)


# Register blueprints
from jvdb.api import piece_api, piece_serie_api
from jvdb.views.views import views_blueprint
from jvdb.views.admin import admin_blueprint
from jvdb.views.login import login_blueprint

app.register_blueprint(piece_api)
app.register_blueprint(piece_serie_api)
app.register_blueprint(views_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(login_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.htm'), 404

# Add methods and modules to jinja environment
from jvdb.utils import serialize_sqla, is_multiple
import json
app.jinja_env.globals.update(json=json)
app.jinja_env.globals.update(serialize_sqla=serialize_sqla)
app.jinja_env.globals.update(is_multiple=is_multiple)

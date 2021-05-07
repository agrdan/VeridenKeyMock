from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(DevConfig)
#db = SQLAlchemy(app)

from app.TestApp import test
app.register_blueprint(test, url_prefix="/")

from app.VeridenKey import vk
app.register_blueprint(vk, url_prefix="/veriden-key/api/v1")


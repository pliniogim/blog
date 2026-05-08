# compblog/__init__.py
from flask import Flask
from compblog.core.views import core



app = Flask(__name__)

app.register_blueprint(core)

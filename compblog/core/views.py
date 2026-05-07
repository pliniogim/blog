# core/views.py

from flask import render_template, request, Blueprint

core = Blueprint('core', __nam__)


@core.route('/')
def index():
    # TODO
    return render_template("index.html")


@core.route('/info')
def info():
    return render_template('info.html')
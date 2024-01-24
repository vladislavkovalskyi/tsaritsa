from flask import render_template
from . import index_blueprint


@index_blueprint.route("/")
def index():
    return render_template("index.html")

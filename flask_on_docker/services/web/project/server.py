from flask import Flask, jsonify, send_from_directory, \
    request, flash, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object("project.config.Config")     # configs - for now stuff that tells Flask where's the DB at
db = SQLAlchemy(app)                    # our db connector I presume


### DB model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, email):
        self.email = email



### API    endpoints

@app.route("/")
def hello_world():
    return jsonify(hello="world!!!")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

@app.route("/media/<path:filename>")
def media_files(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)

# a better approach from flask docs
@app.route("/upload", methods=["GET", "POST"])
def upload_file_2():

    # this actually is useless - because it's nginx who manages those
    if request.method == "POST":
        if "file" not in request.files:
            flash("no file part! select a file.")
            # return redirect(request.url)
            return "wrong call"
        file = request.files["file"]
        if file.filename == "":
            flash("empty file!")
            # return redirect(request.url)
            return "wrong call"
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    # flash("congrats! this worked")
    return render_template("upload.html")

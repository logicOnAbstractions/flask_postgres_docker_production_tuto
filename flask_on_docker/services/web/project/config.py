import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # sqlite being default value if the envars DATABSE_URL isn't set
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"

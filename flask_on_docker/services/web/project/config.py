import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # sqlite being default value if the envars DATABSE_URL isn't set
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABAE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

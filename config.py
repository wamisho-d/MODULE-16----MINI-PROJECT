import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "postgresql+psycopg2://<user>:<password>@<host>:<port>/<database>"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

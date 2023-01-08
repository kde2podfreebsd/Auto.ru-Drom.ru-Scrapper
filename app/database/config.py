import os
from flask import Flask

database_name = "autoparser"

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"postgresql://root:root@172.29.0.2:5432/{database_name}")
SQLALCHEMY_TRACK_MODIFICATIONS = False
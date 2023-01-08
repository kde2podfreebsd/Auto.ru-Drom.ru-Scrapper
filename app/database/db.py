import os
import click
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

database_name = 'autoparser'

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"postgresql://root:root@172.28.0.2:5432/{database_name}")
SQLALCHEMY_TRACK_MODIFICATIONS = False
conn = SQLAlchemy()

app.app_context().push()
app.config['JSON_AS_ASCII'] = False

conn.init_app(app)


@app.cli.command("create_db")
@click.option('-name', default="autodb")
def create_db(name):
    print("creating db %s " % name)
    conn.drop_all()
    conn.create_all()
    conn.session.commit()

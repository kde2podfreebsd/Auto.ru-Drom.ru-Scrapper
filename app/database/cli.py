import click
from flask import Blueprint
from .db import conn
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../'))
from models import Advertisement

bp = Blueprint('commands', __name__)

@bp.cli.command("create_db")
@click.option('-name', default="autoparser")
def create_db(name):
    print("creating db %s " % name)
    conn.drop_all()
    conn.create_all()
    conn.session.commit()
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../'))

from database import app, conn
from typing import Optional

class Advertisement(conn.Model):
    id = conn.Column(conn.Integer, primary_key=True)


    def __repr__(self):
        return '<Advertisement %r>' % self.id
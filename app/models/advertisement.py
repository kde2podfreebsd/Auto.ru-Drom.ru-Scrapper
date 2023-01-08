import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../'))

from database import app, conn
from typing import Optional

class Advertisement(conn.Model):
    id = conn.Column(conn.Integer, primary_key=True)
    title = conn.Column(conn.String(256), nullable=False)
    href = conn.Column(conn.Text, nullable=False)
    price = conn.Column(conn.Text, nullable=False)
    details = conn.Column(conn.Text, nullable=False)
    milage = conn.Column(conn.Text, nullable=True)
    year = conn.Column(conn.Text, nullable=True)
    service = conn.Column(conn.String(8), nullable=False)
    is_send = conn.Column(conn.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Advertisement %r>' % self.id

    def create(self,
               title: str,
               href: str,
               price: str,
               details: str,
               service: str,
               is_send: bool,
               milage: Optional[str] = None,
               year: Optional[str] = None,
               ):
        """
        create account
        """

        with app.app_context():
            if Advertisement.query.filter_by(href=href).first():
                return {"status": False, "msg": "Advertisement already exist"}
            else:
                self.title = title
                self.href = href
                self.price = price
                self.details = details
                self.service = service
                self.is_send = is_send
                self.milage = milage if milage is not None else None
                self.year = year if year is not None else None

                conn.session.add(self)
                conn.session.commit()

                return {"status": True, "msg": "Advertisement created"}


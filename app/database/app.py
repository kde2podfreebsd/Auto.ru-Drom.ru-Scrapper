from .config import app
from .db import conn
from .cli import bp

database_name = 'autoparser'

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://root:root@172.29.0.2:5432/{database_name}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

app.app_context().push()
app.config['JSON_AS_ASCII'] = False

conn.init_app(app)

app.register_blueprint(bp)

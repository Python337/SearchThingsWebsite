from datetime import datetime

from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(85))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()
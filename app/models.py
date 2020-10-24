from app import db
from datetime import datetime


class Comment(db.Model):
    """Data model for posts."""

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    comment = db.Column(db.Text(20), nullable=False)

    def __repr__(self):
        return f"Comment({self.date_posted}', '{self.comment}')"

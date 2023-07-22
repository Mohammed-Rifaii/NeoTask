from sqlalchemy import inspect
from sqlalchemy.orm import validates

from .. import db

class Tasks(db.Model):
# Auto Generated Field(Id):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

# Input by User Fields:
    title       = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed   = db.Column(db.Boolean, nullable=False)
    priority    = db.Column(db.Text,nullable=False)
    duedate     = db.Column(db.Text,nullable=False)
    category    = db.Column(db.Text,nullable=False)

# Converting From Query To Json
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
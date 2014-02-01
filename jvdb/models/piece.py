"""piece.py - Product model."""
from jvdb import db
from jvdb.utils.base_model import BaseEntity


class Piece(db.Model, BaseEntity):
    """Piece model."""
    __tablename__ = 'piece'

    prints = ['id', 'name']
    name = db.Column(db.String(256))
    description = db.Column(db.Text)
    location = db.Column(db.String(256))

    def __init__(self, name='', description='', location=''):
        self.name = name
        self.description = description
        self.location = location

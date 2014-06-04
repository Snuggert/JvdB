"""piece.py - Product model."""
from jvdb import db
from jvdb.utils.base_model import BaseEntity


class PieceSerie(db.Model, BaseEntity):
    """Piece model."""
    __tablename__ = 'piece_serie'

    prints = ['id', 'name']

    name = db.Column(db.String(256))
    pieces = db.relationship('Piece', backref='piece_serie')

    def __init__(self, name=''):
        self.name = name

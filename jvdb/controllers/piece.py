"""piece.py - Controller calls for pieces."""
from jvdb import db
from jvdb.models import Piece


class PieceController:
    """The Controller for piece manipulation."""
    @staticmethod
    def create(piece_dict):
        """Create piece."""
        print piece_dict
        piece = Piece.new_dict(piece_dict)

        db.session.add(piece)
        db.session.commit()

        return piece

    @staticmethod
    def get(piece_id):
        """Get a piece by its id."""
        return Piece.query.get(piece_id)

    @staticmethod
    def update(piece_dict):
        piece = Piece.merge_dict(piece_dict)
        db.session.add(piece)
        db.session.commit()

        return piece

    @staticmethod
    def get_all():
        """Get all pieces."""
        return Piece.query.all()

    @staticmethod
    def delete(piece):
        """ Delete product item """
        db.session.delete(piece)
        db.session.commit()

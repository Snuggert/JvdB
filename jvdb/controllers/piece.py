"""piece.py - Controller calls for pieces."""
from jvdb import db
from jvdb.models import Piece


class PieceController:
    """The Controller for piece manipulation."""

    @staticmethod
    def create(piece_dict):
        """Create piece."""
        piece = Piece.new_dict(piece_dict)
        piece.piece_serie_id = int(piece_dict['piece_serie_id'])
        db.session.add(piece)
        db.session.commit()
        return piece

    @staticmethod
    def get(piece_id):
        """Get a piece by its id."""
        return Piece.query.get(piece_id)

    @staticmethod
    def update(piece_dict):
        """Update a piece."""
        piece = Piece.merge_dict(piece_dict)
        db.session.add(piece)
        db.session.commit()

        return piece

    @staticmethod
    def by_piece_serie(piece_serie_id):
        """Request pieces by series."""
        return Piece.query.filter(Piece.piece_serie_id == piece_serie_id).all()

    @staticmethod
    def get_all():
        """Get all pieces."""
        return Piece.query.all()

    @staticmethod
    def delete(piece):
        """Delete piece item."""
        db.session.delete(piece)
        db.session.commit()

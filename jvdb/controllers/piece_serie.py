"""piece_serie.py - Controller calls for piece_series."""
from jvdb import db
from jvdb.models import PieceSerie


class PieceSerieController:
    """The Controller for piece_serie manipulation."""

    @staticmethod
    def create(piece_serie_dict):
        """Create piece_serie."""
        piece_serie = PieceSerie.new_dict(piece_serie_dict)

        db.session.add(piece_serie)
        db.session.commit()

        return piece_serie

    @staticmethod
    def get(piece_serie_id):
        """Get a piece_serie by its id."""
        return PieceSerie.query.get(piece_serie_id)

    @staticmethod
    def update(piece_serie_dict):
        """Update a piece_serie."""
        piece_serie = PieceSerie.merge_dict(piece_serie_dict)
        db.session.add(piece_serie)
        db.session.commit()

        return piece_serie

    @staticmethod
    def get_all():
        """Get all piece_series."""
        return PieceSerie.query.all()

    @staticmethod
    def delete(piece_serie):
        """Delete piece serie."""
        db.session.delete(piece_serie)
        db.session.commit()

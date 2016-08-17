"""views.py - View for administration."""
from flask import render_template, Blueprint, redirect, url_for
from jvdb.controllers import PieceController, PieceSerieController
from jvdb.utils import row2dict

views_blueprint = Blueprint('views', __name__, url_prefix='')


@views_blueprint.context_processor
def append_piece_series():
    """Append the piece series for all views."""
    piece_series = PieceSerieController.get_all()
    return dict(piece_series=piece_series)


@views_blueprint.route('/', methods=['GET'])
def home():
    """Route for home viewing."""
    return redirect(url_for('views.works',
                            serie=PieceSerieController.get_all()[0].id))


@views_blueprint.route('/works/<int:serie>', methods=['GET'])
def works(serie=1):
    """Route for works viewing."""
    sql_pieces = PieceController.by_piece_serie(serie)
    pieces = []
    for sql_piece in sql_pieces:
        piece = row2dict(sql_piece)
        piece['location'] = piece['location'].replace('./jvdb', '')
        pieces.append(piece)
    return render_template('works.htm', data={'pieces': pieces, })


@views_blueprint.route('/contact', methods=['GET'])
def contact():
    """Route for contact viewing."""
    return render_template('contact.htm')


@views_blueprint.route('/cv', methods=['GET'])
def cv():
    """Route for Curriculum Vitae viewing."""
    return render_template('cv.htm')

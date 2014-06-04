"""views.py - View for administration."""
from flask import render_template, Blueprint
from jvdb.controllers import PieceController
from jvdb.utils import row2dict

views_blueprint = Blueprint('views', __name__, url_prefix='')


@views_blueprint.route('/works', methods=['GET'])
def works():
    sql_pieces = PieceController.get_all()
    pieces = []
    for sql_piece in sql_pieces:
        piece = row2dict(sql_piece)
        piece['location'] = piece['location'].replace('./jvdb', '')
        pieces.append(piece)
    return render_template('works.htm', data={'pieces': pieces, })


@views_blueprint.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.htm')


@views_blueprint.route('/cv', methods=['GET'])
def cv():
    return render_template('cv.htm')

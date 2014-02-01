"""admin.py - View for administration."""
from flask import render_template, Blueprint
from jvdb.controllers import PieceController

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blueprint.route('/piece', methods=['GET'])
def view_pieces():
    pieces = PieceController.get_all()
    return render_template('admin/pieces.htm', data={'pieces': pieces, })


@admin_blueprint.route('/piece/new', methods=['GET'])
def new_piece():
    return render_template('admin/new_piece.htm')

"""admin.py - View for administration."""
from flask import render_template, Blueprint
from jvdb.views import login

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blueprint.route('/piece', methods=['GET'])
@login.login_redirect
def view_pieces():
    return render_template('admin/piece.htm')


@admin_blueprint.route('/piece_serie', methods=['GET'])
def view_piece_series():
    return render_template('admin/piece_serie.htm')

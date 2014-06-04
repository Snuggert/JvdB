"""piece.py - Controller for Piece."""
import os
from flask import Blueprint, jsonify, request
from jvdb.controllers import PieceController
from jvdb.utils import serialize_sqla
from werkzeug.utils import secure_filename

piece_api = Blueprint('piece_api', __name__, url_prefix='/api/piece')


@piece_api.route('', methods=['POST'])
def create():
    """ Create new piece """
    piece_dict = request.json
    PieceController.create(piece_dict)
    return jsonify()


@piece_api.route('/upload', methods=['POST'])
def upload_picture():
    """ Add new picture """
    file = request.files.get('file')
    if file.filename.endswith(".jpg") or file.filename.endswith(".JPG"):
        file_location_name = os.path.join("./jvdb/static/img/",
                                          secure_filename(file.filename))
        file.save(file_location_name)

    return jsonify(location=file_location_name)


@piece_api.route('/<int:piece_id>', methods=['DELETE'])
def delete(piece_id):
    """ Delete piece """
    piece = PieceController.get(piece_id)

    if not piece:
        return jsonify(error='Piece not found'), 500

    PieceController.delete(piece)

    return jsonify()


@piece_api.route('/<int:piece_id>', methods=['GET'])
def get(piece_id):
    """ Get piece """
    piece = PieceController.get(piece_id)

    if not piece:
        return jsonify(error='Piece not found'), 500

    return jsonify(piece=serialize_sqla(piece))


@piece_api.route('/<int:piece_id>', methods=['PUT'])
def edit(piece_id):
    """ Edit piece """
    piece_dict = request.json
    PieceController.update(piece_dict)

    return jsonify()


@piece_api.route('/all', methods=['GET'])
def get_all():
    """ Get all pieces unfiltered """
    # At this point, the association_id should be gotten, so that not ALL
    # pieces are listed, but only those related to the relevant association.
    pieces = PieceController.get_all()

    if not pieces:
        return jsonify(pieces=[])

    return jsonify(pieces=serialize_sqla(pieces))

"""piece_serie.py - Controller for PieceSerie."""
from flask import Blueprint, jsonify, request
from jvdb.controllers import PieceSerieController
from jvdb.utils import serialize_sqla

piece_serie_api = Blueprint('piece_serie_api', __name__,
                            url_prefix='/api/piece_serie')


@piece_serie_api.route('', methods=['POST'])
def create():
    """ Create new piece serie """
    piece_serie_dict = request.json
    PieceSerieController.create(piece_serie_dict)
    return jsonify()


@piece_serie_api.route('/<int:piece_serie_id>', methods=['DELETE'])
def delete(piece_serie_id):
    """ Delete piece serie """
    piece_serie = PieceSerieController.get(piece_serie_id)

    if not piece_serie:
        return jsonify(error='PieceSerie not found'), 500

    PieceSerieController.delete(piece_serie)

    return jsonify()


@piece_serie_api.route('/<int:piece_serie_id>', methods=['GET'])
def get(piece_serie_id):
    """ Get piece serie """
    piece_serie = PieceSerieController.get(piece_serie_id)

    if not piece_serie:
        return jsonify(error='PieceSerie not found'), 500

    return jsonify(piece_serie=serialize_sqla(piece_serie))


@piece_serie_api.route('/<int:piece_serie_id>', methods=['PUT'])
def edit(piece_serie_id):
    """ Edit piece serie """
    piece_serie_dict = request.json
    PieceSerieController.update(piece_serie_dict)

    return jsonify()


@piece_serie_api.route('/all', methods=['GET'])
def get_all():
    """ Get all piece series unfiltered """
    piece_series = PieceSerieController.get_all()

    if not piece_series:
        return jsonify(piece_series=[])

    return jsonify(piece_series=serialize_sqla(piece_series))

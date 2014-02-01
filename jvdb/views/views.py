"""views.py - View for administration."""
import os
import posixpath
from flask import render_template, Blueprint

views_blueprint = Blueprint('views', __name__, url_prefix='')


@views_blueprint.route('/works', methods=['GET'])
def works():
    images = []
    for root, dirs, files in os.walk("./jvdb/static/img/"):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".JPG"):
                images.append(posixpath.normcase(
                              posixpath.join(root, file)).replace("./jvdb",
                                                                  ""))
    return render_template('works.htm', data={'images': images, })

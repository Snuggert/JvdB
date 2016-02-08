"""fill_db.py - Fill the database.

This script fills the database with dummy data, which makes it easier to test
the system.

"""
from jvdb import db
from jvdb.models import *

root = Account('jvdb', '12345')

db.session.add(root)
db.session.commit()

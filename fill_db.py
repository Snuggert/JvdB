"""fill_db.py - Fill the database.

This script fills the database with dummy data, which makes it easier to test
the system.

"""
from app import db
from jvdb.models import *
from werkzeug.security import generate_password_hash

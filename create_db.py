"""create_db.py - Initialize the database.

This script removes any existing databases (app/*.sqlite and
app/*.db). It then uses SQLAlchemy to create tables for all models in the
application.

"""
from jvdb import db
import os
from glob import glob

filelist = glob("app/*.sqlite")
filelist += (glob("app/*.db"))
for f in filelist:
    os.remove(f)

db.create_all()
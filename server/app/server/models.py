from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Brand(db.Model):

    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    __tableargs__ = db.UniqueConstraint('id', 'name', name="unique_brand")

class Beer(db.Model):
    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    brand = db.Column(db.String, db.ForeignKey('brands.name'))
    abv = db.Column(db.Float)

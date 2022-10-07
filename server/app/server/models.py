from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Beer(db.Model):
    __tablename__ = 'beer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    brand = db.Column(db.String, db.ForeignKey('brand.name'))
    abv = db.Column(db.Float)

class Brand(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
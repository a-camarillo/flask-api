import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.queries import beers_list, beer_single, brands_list, brand_single

def create_app(test_config=None):

    app = Flask(__name__,instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
    
    if test_config is None:
        #configuration for use when not testing
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
    else:
        #setting up config for testing
        app.config.from_mapping(test_config)

    from .models import db
    db.init_app(app)    

    @app.route('/')
    def hello():
        return {
            'user': 'MF DOOM',
            'nickname': 'Viktor Vaughn'
        }
    
    @app.route('/beers/', methods=['GET'])
    def get_beers():
        beers = beers_list(db)
        return beers

    @app.route('/beers/<int:id>', methods=['GET'])
    def get_beer(id):
        beer = beer_single(db,id)
        return beer

    @app.route('/brands/', methods=['GET'])
    def get_brands():
        brands = brands_list(db)
        return brands

    @app.route('/brands/<int:id>', methods=['GET'])
    def get_brand(id):
        brand = brand_single(db,id)
        return brand


    return app


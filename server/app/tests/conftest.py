import os

import pytest

from server import create_app
from server.models import Beer, Brand, db

from data import populate_db

@pytest.fixture()
def app():

    app = create_app(test_config={'TESTING':True})
    #app.config['TESTING'] = True

    db.init_app(app)
    # creating a new database for the unit test
    with app.app_context():
        db.create_all()
        populate_db(db)
    
    yield app

    # tear down the database
    with app.app_context():
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def new_beer():
    beer = Beer(name='Wahoo',brand='Ballast Point',abv=4.5)
    return beer

@pytest.fixture(scope='module')
def new_brand():
    brand = Brand(name='Alamo')
    return brand
from server.models import Beer, Brand
"""
This file will be used to create test data and populate the test database with the test data
"""

test_brand_1 = Brand(name='Alamo')
test_brand_2 = Brand(name='Duff')

test_beer_1 = Beer(name='test beer 1',brand='Alamo',abv=3.4)
test_beer_2 = Beer(name='test beer 2',brand='Duff',abv=4)

def populate_db(db):
    db.session.add(test_brand_1)
    db.session.add(test_brand_2)
    db.session.add(test_beer_1)
    db.session.add(test_beer_2)
    db.session.commit()

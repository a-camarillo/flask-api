def test_new_beer(new_beer)
""" 
GIVEN a Beer model
WHEN a new Beer is created
THEN check the name, brand, and abv are defined correctly
"""
assert new_beer.name == 'Wahoo'
assert new_beer.brand == 'Ballast Point'
assert new_beer.abv == 4.5
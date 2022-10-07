from flask import jsonify
from .models import Beer, Brand

def beers_list(db):
    total_beers = {}
    beers = db.session.execute(db.select(Beer).order_by(Beer.name)).scalars().all()
    for beer in beers:
        beer_dict = {}
        beer_dict['id'] = beer.id
        beer_dict['name'] = beer.name
        beer_dict['brand'] = beer.brand
        beer_dict['abv'] = beer.abv
        total_beers[f'{beer.id}'] = beer_dict
    return total_beers
    
def beer_single(db,id):
    beer_dict = {}
    beer = db.session.execute(db.select(Beer).where(Beer.id==id)).scalar()
    if beer is None:
        return {'Error': 'A resource with this id does not exist'}
    beer_dict['id'] = beer.id
    beer_dict['name'] = beer.name
    beer_dict['brand'] = beer.brand
    beer_dict['abv'] = beer.abv
    return beer_dict

def brands_list(db):
    total_brands = {}
    brands = db.session.execute(db.select(Brand).order_by(Brand.name)).scalars().all()
    for brand in brands:
        brand_dict = {}
        brand_dict['id'] = brand.id
        brand_dict['name'] = brand.name
        total_brands[f'{brand.id}'] = brand_dict
    return total_brands

def brand_single(db,id):
    brand_dict = {}
    brand = db.session.execute(db.select(Brand).where(Brand.id==id)).scalar()
    brand_dict['id'] = brand.id
    brand_dict['name'] = brand.name
    return brand_dict
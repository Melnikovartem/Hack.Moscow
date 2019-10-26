import requests
from declarator_generator import declarator_generator
API = 'https://declarator.org/api/v1/search/sections'

# Usage example
# RealEstateParser.request_real_estate(region=64) returns list of
# {square:xxx, year:xxx, person: {id:xxx, name:xxx}}
class RealEstateParser:
    @staticmethod
    def simplify_section(section):
        square = 0
        for est in section['real_estates']:
            square += est['square']
        return {
            'square': square,
            'year': section['main']['year'],
            'person': {
                'id': section['main']['person']['id'],
                'name': section['main']['person']['name']
            }
        }
    @staticmethod
    def request_real_estate(**params):
        resp = requests.get(API, params)
        for item in declarator_generator(resp):
            return RealEstateParser.simplify_section(item)

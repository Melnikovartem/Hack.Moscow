import requests

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
    def request_real_estate(pages = None, **params):
        res = requests.get(API, params).json()
        i = 1
        while res['next'] is not None:
            print('Getting page {}'.format(i))
            for section in map(RealEstateParser.simplify_section, res['results']):
                yield section
            i += 1
            if pages is not None and i > pages:
                break
            res = requests.get(res['next']).json()

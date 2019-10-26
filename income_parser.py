import requests
from declarator_generator import declarator_generator

API = 'https://declarator.org/api/v1/search/sections'

# Usage example
# IncomeParser.request_income(region=64) returns list of
# {income:xxx, year:xxx, person: {id:xxx, name:xxx}}
class IncomeParser:
    @staticmethod
    def simplify_section(section):
        income = 0
        for inc in section['incomes']:
            income += inc['size']
        return {
            'income': income,
            'year': section['main']['year'],
            'person': {
                'id': section['main']['person']['id'],
                'name': section['main']['person']['name']
            }
        }
    @staticmethod
    def request_income(**params):
        resp = requests.get(API, params)
        for item in declarator_generator(resp):
            yield IncomeParser.simplify_section(item)

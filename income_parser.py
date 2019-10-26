import requests

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
    def request_income(pages = None, **params):
        res = requests.get(API, params).json()
        i = 1
        while res['next'] is not None:
            print('Getting page {}'.format(i))
            for section in map(IncomeParser.simplify_section, res['results']):
                yield section
            i += 1
            if pages is not None and i > pages:
                break
            res = requests.get(res['next']).json()

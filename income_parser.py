import requests

API = 'https://declarator.org/api/v1/search/sections'

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
        res = requests.get(API, params).json()
        sections = []
        i = 1
        while res['next'] is not None:
            print('Getting page {}'.format(i))
            sections += list(map(IncomeParser.simplify_section, res['results']))
            res = requests.get(res['next']).json()
            i += 1
        return sections
        

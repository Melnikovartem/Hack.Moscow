import requests
def declarator_generator(response):
    for res in response.json()['results']:
        yield res
    print('Gettings the rest')
    while response.json()['next'] is not None:
        response = requests.get(response.json()['next'])
        for res in response.json()['results']:
            yield res


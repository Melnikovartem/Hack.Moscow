from sklearn.ensemble import IsolationForest
import requests
def declarator_generator(response):
    for res in response.json()['results']:
        yield res
    while response.json()['next'] is not None:
        response = requests.get(response.json()['next'])
        for res in response.json()['results']:
            yield res

def root_office(office, up, parent):
    for i in range(up):
        if office in parent:
            office = parent[office]
        else:
            return office
    return office
def single_office_data(office, with_relatives = False):
    for res in declarator_generator(requests.get(API, {'office': office})):
        income = 0
        for inc in res['incomes']:
            if with_relatives or inc['relative'] is None:
                income += inc['size']
        square = 0
        for est in res['real_estates']:
            if with_relatives or est['relative'] is None:
                if est['square'] is not None:
                    square += est['square']
        yield {'id' : res['main']['person']['id'], 'income': income, 'square': square}
def recursive_office_data(office, tree, with_relatives = False):
    for res in single_office_data(office, with_relatives):
        yield res
    for child in tree.get(office, []):
        for res in recursive_office_data(child, with_relatives):
            yield res
def outlier_k(incomes):
    data = pd.DataFrame(incomes).set_index('id')
    model = IsolationForest(n_estimators=200)
    return (1 - sum(list(map(lambda x: max(x, 0),model.fit_predict(data)))) / len(data)) ** 2

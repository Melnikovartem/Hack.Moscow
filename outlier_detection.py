import pandas as pd
import numpy as np
from income_parser import IncomeParser
from declarator_generator import declarator_generator
import requests
API = 'https://declarator.org/api/v1/search/sections'

from sklearn.ensemble import IsolationForest

offices = pd.read_csv('offices.csv', sep=';').set_index('id')
tree, parent = {}, {}
for row in offices['parent_id'].items():
    if not np.isnan(row[1]):
        a, b = int(row[0]), int(row[1])
        if b not in tree:
            tree[b] = []
        tree[b].append(a)
        parent[a] = b

def root_office(office, up = 2):
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
def recursive_office_data(office, with_relatives = False):
    for res in single_office_data(office, with_relatives):
        yield res
    for child in tree.get(office, []):
        for res in recursive_office_data(child, with_relatives):
            yield res
def outlier_k(incomes):
    data = pd.DataFrame(incomes).set_index('id')
    model = IsolationForest(n_estimators=200)
    return (1 - sum(list(map(lambda x: max(x, 0),model.fit_predict(data)))) / len(data)) ** 2
def office_id_to_outlier_k(office):
    return outlier_k(list(recursive_office_data(root_office(office))))

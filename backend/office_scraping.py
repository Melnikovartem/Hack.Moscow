import pandas as pd
import numpy as np
import pickle

def make_office_names():
    return pickle.load(open('office_names.dump', 'rb'))
def to_office_pair(office, office_names):
    return {'id' : office, 'name': office_names[office]}
def make_region_lists():
    region_to_offices = {}
    data = pd.read_csv('offices_reg.csv', sep=';').set_index('id')
    office_names = make_office_names()
    for id, region in data['region_id'].items():
        if not np.isnan(region):
            id, region = int(id), int(region)
            if region not in region_to_offices:
                region_to_offices[region] = []
            region_to_offices[region].append(to_office_pair(id, office_names))
    return region_to_offices
def tree_unfold():
    tree, parent = pickle.load(open('tree_parent.dump', 'rb'))
    office_names = make_office_names()
    unfold = {}
    def recursive_children(node):
        if node not in tree:
            return []
        res = []
        for innode in tree[node]:
            res.append(to_office_pair(innode, office_names))
            res += recursive_children(innode)
        return res
    for office in parent.keys():
        root = office
        while root in parent:
            root = parent[root]
        if root in unfold:
            continue
        unfold[root] = recursive_children(root)
    return unfold

if __name__ == '__main__':
    print(make_region_lists())

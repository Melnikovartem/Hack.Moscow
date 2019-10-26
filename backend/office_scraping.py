import pandas as pd
import numpy as np
import pickle

def make_region_lists():
    region_to_offices = {}
    data = pd.read_csv('offices2.csv', sep=';').set_index('id')
    for id, region in data['region_id']:
        if type(region) == str:
            id, region = int(id), int(region)
            if region not in region_to_offices:
                region_to_offices[region] = []
            region_to_offices[region].append(id)
    return region_to_offices
def tree_unfold():
    tree, parent = pickle.load(open('tree_parent', 'rb'))
    unfold = {}
    def recursive_children(node):
        if node not in tree:
            return
        res = []
        for innode in tree[node]:
            res.append(innode)
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

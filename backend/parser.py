def make_tree_parent():
    import numpy as np
    import pandas as pd
    offices = pd.read_csv('offices.csv', sep=';').set_index('id')
    tree, parent = {}, {}
    for row in offices['parent_id'].items():
        if not np.isnan(row[1]):
            a, b = int(row[0]), int(row[1])
            if b not in tree:
                tree[b] = []
            tree[b].append(a)
            parent[a] = b
    return tree, parent


class office_data:
    ask = "https://declarator.org/api/v1/search/sections/?office="
    
    def find_children(self):
        tree, _ = make_tree_parent()
        return tree[self.office_id] 
#     def __init__(self, data):
#         self.data = data

    def __init__(self, office_id):
        self.office_id = office_id
        data_struct = {} 
        data = {'next':self.ask+str(office_id)}

        while data["next"]:
            with urllib.request.urlopen(data["next"]) as url:
                data = json.loads(url.read().decode())
            for i in data["results"]:
                if i["main"]["year"] not in data_struct:
                    data_struct[i["main"]["year"]] = []
                data_struct[i["main"]["year"]].append(i)
            print(data["next"])
#         #надо обойти всех child и вызвать одну из функций sort
#         child_list = self.find_children()
#         for i in child_list:
#             child_data = get_data_office(i)
#             for j in child_data:
#                 if j not in data_struct:
#                     data_struct[j] = []
#                 data_struct[j] += child_data[j]

        self.data = data_struct # данные всех деклараций по годам
        self.family = 0 # учитывать ли семью
        
    def true_avg(self):
        years = self.data.keys()
        res = [0]  * len(years)
        for i, year in enumerate(years):
            curr_sum = 0
            curr_amount = 0
            for declaration in self.data[year]:
                inc = declaration['incomes'][0]['size']
                if inc == inc:
                    curr_amount += 1
                    curr_sum += inc
            if curr_amount != 0:
                res[i] = curr_sum / curr_amount
        return res
        
    def gender_avg(self):
        years = self.data.keys()
        males = [0] * len(years)
        females = [0] * len(years)
        for i, year in enumerate(years):
            male_sum = 0
            female_sum = 0
            male_amount = 0
            female_amount = 0
            for declaration in self.data[year]:
                gender = declaration['main']['person']['gender']
                inc = declaration['incomes'][0]['size']
                if inc == inc:
                    if gender == 'M':
                        male_sum += inc
                        male_amount += 1
                    elif gender == 'F':
                        female_sum += inc
                        female_amount += 1
            if male_amount != 0:
                males[i] = male_sum / male_amount
            if female_amount != 0:
                females[i] = female_sum / female_amount
        return males, females
        
    def party_avg(self):
        parties = set()
        years = self.data.keys()
        for year in years:
            for declaration in self.data[year]:
                party = declaration['main']['party']
                if party != party or party == None:
                    parties.add('Н.Д.')
                else:
                    parties.add(party['name'])
        return parties
    def outlier_k(self):
        from sklearn.ensemble import IsolationForest
        import requests
        tree, parent = make_tree_parent()
        def declarator_generator(response):
            for res in response.json()['results']:
                yield res
            while response.json()['next'] is not None:
                response = requests.get(response.json()['next'])
                for res in response.json()['results']:
                    yield res

        def root_office(office, up):
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
        return outlier_k(list(
            recursive_office_data(root_office(office, 1))
        ))
    #self.data - список по годам деклараций людей

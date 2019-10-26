import pickle
from outlier_detection import *
import urllib, requests, json

def savings_format():
    return float(saving_str[:saving_str.find('руб.')-1].replace(' ', '').replace(',', '.'))

def make_tree_parent():
    import pickle
    return pickle.load(open('tree_parent.dump', 'rb'))

def find_children(office_id):
    tree, _ = make_tree_parent()
    if office_id in tree:
        return tree[self.office_id]
    else:
        return []

def get_data_office(x):
    data_struc = {}
    data = {'next':"https://declarator.org/api/v1/search/sections/?office="+str(x)}

    while data["next"]:
        with urllib.request.urlopen(data["next"]) as url:
            data = json.loads(url.read().decode())
        for i in data["results"]:
            if i["main"]["year"] not in data_struc:
                data_struc[i["main"]["year"]] = []
            data_struc[i["main"]["year"]].append(i)
    #надо обойти всех child и вызвать одну их функций из пред ячейки
    child_list = find_children(x)
    for i in child_list:
        child_data = get_data_office(i)
        for j in child_data:
            if j not in data_struc:
                data_struc[j] = []
            data_struc[j] += child_data[j]

    return data_struc

class office_data:
    ask = "https://declarator.org/api/v1/search/sections/?office="


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
        #надо обойти всех child и вызвать одну из функций sort
        child_list = find_children(office_id)
        for i in child_list:
            child_data = get_data_office(i)
            for j in child_data:
                if j not in data_struct:
                    data_struct[j] = []
                data_struct[j] += child_data[j]

        self.data = data_struct # данные всех деклараций по годам
        self.family = 0 # учитывать ли семью

    def true_avg(self, typ):
        years = self.data.keys()
        res = [None]  * len(years)
        for i, year in enumerate(years):
            curr_sum = 0
            curr_amount = 0
            for declaration in self.data[year]:
                for pep in declaration[typ]:
                    inc = pep['size']
                    if self.family or (pep['relative'] == None):
                        if inc != None:
                            curr_sum += inc
                curr_amount += 1
            if curr_amount != 0:
                res[i] = curr_sum / curr_amount
        return res
    
    def gender_avg(self, typ):
        years = self.data.keys()
        males = [None] * len(years)
        females = [None] * len(years)
        for i, year in enumerate(years):
            male_sum = 0
            female_sum = 0
            male_amount = 0
            female_amount = 0
            for declaration in self.data[year]:
                gender = declaration['main']['person']['gender']
                for pep in declaration[typ]:
                    inc = pep['size']
                    if self.family or (pep['relative'] == None):
                        if inc != None:
                            if gender == 'M':
                                male_sum += inc
                            elif gender == 'F':
                                female_sum += inc
                if gender == 'M':
                    male_amount += 1
                elif gender == 'F':
                    female_amount += 1
            if male_amount != 0:
                males[i] = male_sum / male_amount
            if female_amount != 0:
                females[i] = female_sum / female_amount
        
        return males, females
        
    def party_avg(self, typ):
        parties = set()
        years = self.data.keys()
        for year in years:
            for declaration in self.data[year]:
                party = declaration['main']['party']
                if party != party or party == None:
                    parties.add('Нет Данных')
                else:
                    parties.add(party['name'])
        parties = list(parties)
        res = {par : [None] * len(years) for par in parties}
        for i, year in enumerate(years):
            sums = {par : 0 for par in parties}
            amounts = {par : 0 for par in parties}
            for declaration in self.data[year]:
                party = declaration['main']['party']
                if party != party or party == None:
                    party = 'Нет Данных'
                else:
                    party = party['name']
                for pep in declaration[typ]:
                    inc = pep['size']
                    if self.family or (pep['relative'] == None):
                        if inc != None:
                            sums[party] += inc
                amounts[party] += 1
            for party in parties:
                if amounts[party] != 0:
                    res[party][i] = sums[party] / amounts[party]
        return parties, list(res.values())
    
    def outlier_k(self):
        tree, parent = make_tree_parent()
        return outlier_k(list(
            recursive_office_data(root_office(office, 1, parent), tree)
        ))
    #self.data - список по годам деклараций людей
a = office_data(12)
print(a.party_avg("incomes"))

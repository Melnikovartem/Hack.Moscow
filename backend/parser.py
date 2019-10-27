import pickle
from outlier_detection import *
import urllib
import requests
import json
from collections import defaultdict
from math import log10, fabs


def list_to_benford(nums):
    """Returns list of length 10 with frequencies of ocurrance of digits on the first place.
    Order of digits: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    """
    intnums = [int(i) for i in nums]
    benford = {str(i): 0 for i in range(10)}
    for num in intnums:
        str_repr = str(num)
        benford[str_repr[0]] += 1
    benford = sorted(list(benford.items()), key=(
        lambda x: (int(x[0]) + 10) % 11))
    total = len(nums)
    benford = [b[1] / total for b in benford]
    return benford


def create_true_benford():
    """Returns list of length 10 with ideal Benford frequenices.
    Zero (0) is added as 10th element with probability of 0.0"""
    true_benford = [log10(1 + 1 / b) for b in range(1, 10)]
    true_benford.append(0)
    return true_benford


def test_fake(benford, val=0.2):
    """Tests if sum of elementwise difference between values in list 'benford' and ideal Benford frequencies is smaller than val"""
    true_benford = create_true_benford()
    diff = [fabs(a - b) for a, b in zip(benford, true_benford)]
    return sum(diff) >= val


def savings_format(saving_str):
    return float(saving_str[:saving_str.find('руб.') - 1].replace(' ', '').replace(',', '.'))


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
    data = {
        'next': "https://declarator.org/api/v1/search/sections/?office=" + str(x)}

    while data["next"]:
        with urllib.request.urlopen(data["next"]) as url:
            data = json.loads(url.read().decode())
        for i in data["results"]:
            if i["main"]["year"] not in data_struc:
                data_struc[i["main"]["year"]] = []
            data_struc[i["main"]["year"]].append(i)
    # надо обойти всех child и вызвать одну их функций из пред ячейки
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

    def __init__(self, office_id, family):
        self.office_id = office_id
        data_struct = {}
        data = {'next': self.ask + str(office_id)}
        while data["next"]:
            with urllib.request.urlopen(data["next"]) as url:
                data = json.loads(url.read().decode())
            for i in data["results"]:
                if i["main"]["year"] not in data_struct:
                    data_struct[i["main"]["year"]] = []
                data_struct[i["main"]["year"]].append(i)
        self.name = data['results'][0]['main']['office']['name']
        # надо обойти всех child и вызвать одну из функций sort
        child_list = find_children(office_id)
        for i in child_list:
            child_data = get_data_office(i)
            for j in child_data:
                if j not in data_struct:
                    data_struct[j] = []
                data_struct[j] += child_data[j]

        self.type_to_field = {'incomes': 'size', 'real_estates': 'square'}

        self.data = data_struct  # данные всех деклараций по годам
        self.family = family  # учитывать ли семью

    def get_min(self, typ):
        return(min(self.get_arr(typ)))

    def get_max(self, typ):
        return(max(self.get_arr(typ)))

    def get_median(self, typ):
        arr = sorted(self.get_arr(typ))
        return(arr[len(arr) // 2])

    def get_arr(self, typ):
        if typ == 'incomes':
            return self.incomes()
        if typ == 'real_estates':
            return self.real_estates()
        return self.savings()

    def get_benford(self, typ):
        arr = sorted(self.get_arr(typ))
        return list_to_benford(arr)

    def incomes(self):
        res = []
        years = self.data.keys()
        for year in years:
            for declaration in self.data[year]:
                curr = 0
                for pep in declaration['incomes']:
                    inc = pep['size']
                    if self.family or (pep['relative'] == None):
                        if inc != None:
                            curr += inc
                res.append(curr)
        return res

    def real_estates(self):
        res = []
        years = self.data.keys()
        for year in years:
            for declaration in self.data[year]:
                curr = 0
                for pep in declaration['real_estates']:
                    inc = pep['square']
                    if self.family or (pep['relative'] == None):
                        if inc != None:
                            curr += inc
                res.append(curr)
        return res

    def savings(self):
        res = []
        years = self.data.keys()
        for year in years:
            for declaration in self.data[year]:
                curr = 0
                for pep in declaration['savings']:
                    inc = savings_format(pep)
                    if self.family or (pep['relative'] == None):
                        if inc != None:
                            curr += inc
                res.append(curr)
        return res

    def most_common_vehicle(self):
        brands = defaultdict(int)
        years = self.data.keys()
        for year in years:
            for declaration in self.data[year]:
                for pep in declaration['vehicles']:
                    if pep != None:
                        if pep['brand'] != None:
                            brand = pep['brand']['name']
                            if brand != None:
                                brands[pep['brand']['name']] += 1
        if brands.items()!=brands.items():
            return sorted(list(brands.items()), key=(lambda x: -1 * x[1]))[0][0]
        else:
            return "Нет машин"

    def true_avg(self, typ):
        years = self.data.keys()
        res = [None] * len(years)
        for i, year in enumerate(years):
            curr_sum = 0
            curr_amount = 0
            for declaration in self.data[year]:
                if typ == 'vehicles':
                    curr_sum += len(declaration[typ])
                    curr_amount += 1
                elif typ == 'savings':
                    for pep in declaration[typ]:
                        inc = savings_format(pep)
                        if self.family or (pep['relative'] == None):
                            if inc != None:
                                curr_sum += inc
                    curr_amount += 1
                else:
                    for pep in declaration[typ]:
                        inc = pep[self.type_to_field[typ]]
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
                if typ == 'vehicles':
                    if gender == 'M':
                        male_sum += len(declaration[typ])
                    elif gender == 'F':
                        female_sum += len(declaration[typ])
                else:
                    for pep in declaration[typ]:
                        if typ == 'savinngs':
                            inc = savings_format(pep)
                        else:
                            inc = pep[self.type_to_field[typ]]
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
        res = {par: [None] * len(years) for par in parties}
        for i, year in enumerate(years):
            sums = {par: 0 for par in parties}
            amounts = {par: 0 for par in parties}
            for declaration in self.data[year]:
                party = declaration['main']['party']
                if party != party or party == None:
                    party = 'Нет Данных'
                else:
                    party = party['name']
                if typ == 'vehicles':
                    sums[party] += len(declaration[typ])
                    amounts[party] += 1
                else:
                    for pep in declaration[typ]:
                        if typ == 'savinngs':
                            inc = savings_format(pep)
                        else:
                            inc = pep[self.type_to_field[typ]]
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
            recursive_office_data(root_office(self.office_id, 1, parent), tree)
        ))

    def parent(self):
        return make_tree_parent()[1].get(self.office_id)
    # self.data - список по годам деклараций людей

from math import log10
from math import fabs

def list_to_benford(nums):
    """Returns list of length 10 with frequencies of ocurrance of digits on the first place.
    Order of digits: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    """
    intnums = [int(i) for i in nums]
    benford = {str(i) : 0 for i in range(10)}
    for num in intnums:
        str_repr = str(num)
        benford[str_repr[0]] += 1
    benford = sorted(list(benford.items()), key=(lambda x: (int(x[0]) + 10) % 11))
    total = len(nums)
    benford = [b[1] / total for b in benford]
    return benford

def create_true_benford():
    """Returns list of length 10 with ideal Benford frequenices.
    Zero (0) is added as 10th element with probability of 0.0"""
    true_benford = [log10(1 + 1/b) for b in range(1, 10)]
    true_benford.append(0)
    return true_benford

def test_fake(benford, val = 0.2):
    """Tests if sum of elementwise difference between values in list 'benford' and ideal Benford frequencies is smaller than val"""
    true_benford = create_true_benford()
    diff = [fabs(a - b) for a, b in zip(benford, true_benford)]
    return sum(diff) >= val

class office_data:
    ask = "https://declarator.org/api/v1/search/sections/?office="

    def find_children(self):
        return []

    def __init__(self, office_id):
        self.office_id = office_id
        data_struc = {}
        data = {'next':self.ask+str(office_id)}

        while data["next"]:
            with urllib.request.urlopen(data["next"]) as url:
                data = json.loads(url.read().decode())
            for i in data["results"]:
                if i["main"]["year"] not in data_struc:
                    data_struc[i["main"]["year"]] = []
                data_struc[i["main"]["year"]].append(i)
            print(data["next"])
        #надо обойти всех child и вызвать одну из функций sort
        child_list = self.find_children()
        for i in child_list:
            child_data = get_data_office(i)
            for j in child_data:
                if j not in data_struc:
                    data_struc[j] = []
                data_struc[j] += child_data[j]

        self.data = data_struc # данные всех деклараций по годам
        self.family = 0 # учитывать ли семью
    def gender_sort(self):
        pass
    def party_sort(self):
        pass
    def medium_sort(self):
        return self.data
    #self.data - список по годам деклараций людей
#made a kistake in git commit -m FFF

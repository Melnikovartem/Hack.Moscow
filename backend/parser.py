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

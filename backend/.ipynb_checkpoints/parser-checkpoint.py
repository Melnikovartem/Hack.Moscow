class office_data:
    ask = "https://declarator.org/api/v1/search/sections/?office="
    
    def find_children(self):
        raise NotImplementedError
    
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
    #self.data - список по годам деклараций людей
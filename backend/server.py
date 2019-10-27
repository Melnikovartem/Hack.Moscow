from flask import Flask, render_template, request
from parser import office_data

app = Flask(__name__)

#костыльную оптимизацию не убирать
data = {}

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/result/<office_id>', methods=['GET'])
def result(office_id):
    family = request.args.get('family', default=0, type=int)

    if office_id in data:
        office = data[office_id]
    else:
        office = office_data(office_id, family)
        data[office_id] = office
    office.family = family
    avarage_salary = office.true_avg("incomes")
    years = list(office.data)  # просто средняя зарплата

    m_avarage_salary = office.gender_avg("incomes")[0]
    w_avarage_salary = office.gender_avg("incomes")[1]

    savings = office.savings()
    car = office.most_common_vehicle()

    part_names = office.party_avg("incomes")[0]
    part_salaries = office.party_avg("incomes")[1]  # по партиям средняя зарплата

    for s in range(len(w_avarage_salary)):
        if w_avarage_salary[s] == None:
            w_avarage_salary[s] = 'null'

    for s in range(len(m_avarage_salary)):
        if m_avarage_salary[s] == None:
            m_avarage_salary[s] = 'null'
    for s in range(len(avarage_salary)):
        if avarage_salary[s] == None:
            avarage_salary[s] = 'null'

    for salary in part_salaries:

        for s in range(len(salary)):
            if salary[s] == None:
                salary[s] = 'null'
    return render_template("result.html", family=family, avarage_salary=avarage_salary, years=years, m_avarage_salary=m_avarage_salary, w_avarage_salary=w_avarage_salary, part_names=part_names, part_salaries=part_salaries)


if __name__ == "__main__":
    app.run(debug=True)

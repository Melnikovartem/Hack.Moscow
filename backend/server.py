from flask import Flask, render_template, request
from parser import office_data

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/result/', methods=['GET'])
def result():
    office_id = request.args.get('office_id')
    print(request.args.get('family', default=0, type=int))
    family = request.args.get('family', default=0, type=int)

    office = office_data(office_id)
    avarage_salary = office.true_avg("incomes")
    years = list(office.data)  # просто средняя зарплата
    # Пример: [975657.0, 1063445.0, 1215654.67, 1397083.65, 1769658.0, 2213239.15, 3031778.9, 2769537.14, 1567386.81, 1478636.39, 1445398.08]
    m_avarage_salary = office.gender_avg("incomes")[0]
    w_avarage_salary = office.gender_avg("incomes")[1]
    # по полу средняя зарплата
    # Пример: [975657.0, 1063445.0, 1215654.67, 1397083.65, 1769658.0, 2213239.15, 3031778.9, 2769537.14, 1567386.81, 1478636.39, 1445398.08], [None, None, None, None, None, None, None, None, None, None, None]
    part_names = office.party_avg("incomes")[0]
    part_salaries = office.party_avg(
        "incomes")[1]  # по партиям средняя зарплата
    # Пример: (['Нет Данных', 'Единая Россия'], [[None, None, None, None, None, None, None, 2769537.14, 1567386.81, 1478636.39, 1445398.08], [975657.0, 1063445.0, 1215654.67, 1397083.65, 1769658.0, 2213239.15, 3031778.9, None, None, None, None]])

    # Денис скоро добавит остальные функции к
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

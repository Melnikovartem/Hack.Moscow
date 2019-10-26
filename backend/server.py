from flask import Flask, render_template, request
from parser import office_data

app =Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/result/<office_id>')
def result(office_id):
    print(request.args.get('family', default = 0, type = int))
    family = request.args.get('family', default = 0, type = int)
#    office = office_data(office_id, family)
#    print(office.true_avg("incomes")) # просто средняя зарплата
#    # Пример: [975657.0, 1063445.0, 1215654.67, 1397083.65, 1769658.0, 2213239.15, 3031778.9, 2769537.14, 1567386.81, 1478636.39, 1445398.08]
#    print(office.gender_avg("incomes")) # по полу средняя зарплата
    # Пример: [975657.0, 1063445.0, 1215654.67, 1397083.65, 1769658.0, 2213239.15, 3031778.9, 2769537.14, 1567386.81, 1478636.39, 1445398.08], [None, None, None, None, None, None, None, None, None, None, None]
#    print(office.party_avg("incomes")) # по партиям средняя зарплата
    # Пример: (['Нет Данных', 'Единая Россия'], [[None, None, None, None, None, None, None, 2769537.14, 1567386.81, 1478636.39, 1445398.08], [975657.0, 1063445.0, 1215654.67, 1397083.65, 1769658.0, 2213239.15, 3031778.9, None, None, None, None]])

    # Денис скоро добавит остальные функции к
    return render_template("result.html", family=family)

if __name__ == "__main__":
    app.run()

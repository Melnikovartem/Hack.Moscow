from flask import Flask, render_template, request
from parser import office_data
import office_scraping

app = Flask(__name__)

#костыльную оптимизацию не убирать
data = {}

@app.route('/')
def main():
    return render_template("index.html")


def null_change(x):
    for s in range(len(x)):
        if x[s] == None:
            x[s] = 'null'
    return x

@app.route('/result/<office_id>', methods=['GET'])
def result(office_id):
    family = request.args.get('family', default=0, type=int)

    if office_id in data:
        office = data[office_id]
    else:
        office = office_data(office_id, family)
        data[office_id] = office
    office.family = family
    years = list(office.data)


    avg_inc = office.true_avg("incomes")
    avg_est = office.true_avg("real_estates")
    avg_sav = office.true_avg("savings")
    avg_vec = office.true_avg("vehicles")

    normal_data = {'normal': [avg_inc, avg_est, avg_sav, avg_vec]}


    # просто средняя зарплата
    # ЕСБАТЬ ВАС И ВАШИ КОСТЫЛИ ВЫ НАХУЙ НАУЧИТЕСЬ РАБОТАТЬ С АБСТРАЦИЯМИ ИЛИ ИДТИЕ ПИСАЙТ САЙТЫ НА ФРИЛАНС


    m_avg_inc = null_change(office.gender_avg("incomes")[0])
    w_avg_inc = null_change(office.gender_avg("incomes")[1])
    m_avg_est = null_change(office.gender_avg("real_estates")[0])
    w_avg_est = null_change(office.gender_avg("real_estates")[1])
    m_avg_sav = null_change(office.gender_avg("savings")[0])
    w_avg_sav = null_change(office.gender_avg("savings")[1])
    m_avg_vec = null_change(office.gender_avg("vehicles")[0])
    w_avg_vec = null_change(office.gender_avg("vehicles")[1])
    mv_data = {"M": [m_avg_inc, m_avg_est, m_avg_sav, m_avg_vec],
        "F": [w_avg_inc, w_avg_est, w_avg_sav, w_avg_vec]}
    #

    savings = office.savings()
    car = office.most_common_vehicle()
    #


    part_names = office.party_avg("incomes")[0]
    part_inc = null_change(office.party_avg("incomes")[1])
    part_est = null_change(office.party_avg("real_estates")[1])
    part_sav = null_change(office.party_avg("savings")[1])
    part_vec = null_change(office.party_avg("vehicles")[1])
    part_data = {}
    for i in range(len(part_names)):
        part_data[part_names[i]] = [part_inc[i], part_est[i], part_sav[i], part_vec[i]]
    #
    return render_template("result.html", family=family, name=office.name, years=years, normal_data=normal_data, mv_data=mv_data, part_data=part_data)


if __name__ == "__main__":
    app.run()

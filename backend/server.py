from flask import Flask, render_template
from parser import office_data

app =Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/result/<office_id>')
def result(office_id):
    print("CALL", office_id)
    family = 0
    office = office_data(office_id, family)
    print(office.true_avg("incomes"))
    print(office.gender_avg("incomes"))
    print(office.party_avg("incomes"))
    return render_template("result.html")

if __name__ == "__main__":
    app.run()

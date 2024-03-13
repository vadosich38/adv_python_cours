from flask import Flask

app = Flask(__name__)
storage = dict()


@app.route("/add/<date>/<int:number>")
def add_expense(date: str, number: int):
    global storage
    year = int(date[:4])
    month = int(date[4:6])

    storage.setdefault(year, {}).setdefault(month, 0)
    storage[year][month] += number

    storage.setdefault(year, {}).setdefault('total', 0)
    storage[year]['total'] += number

    return f"Принята запись! {storage[year][month]}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    global storage
    storage.setdefault(year, {}).setdefault(month, 0)
    result_summ = storage[year][month]

    return f"Расход за {month} месяц {year} года составляет {result_summ}"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    global storage
    storage.setdefault(year, {}).setdefault('total', 0)
    result_summ = storage[year]['total']

    return f"Расход за {year} год составляет {result_summ}"


if __name__ == "__main__":
    app.run(debug=True)

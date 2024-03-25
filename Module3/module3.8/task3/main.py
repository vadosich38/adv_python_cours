from flask import Flask

app = Flask(__name__)
storage = dict()


@app.route("/add/<date>/<int:number>")
def add_expense(date: str, number: int):
    if len(date) != 8:
        raise TypeError("Введенная дата не соответствует формату 20240101")

    global storage
    year = int(date[:4])
    month = int(date[4:6])
    day_date = int(date[6:8])

    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day_date, 0)
    storage[year][month][day_date] += number

    storage.setdefault(year, {}).setdefault('total', 0)
    storage[year]['total'] += number

    storage.setdefault(year, {}).setdefault(month, {}).setdefault('total', 0)
    storage[year][month]['total'] += number

    return f"Принята запись! {storage[year][month][day_date]}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    global storage
    storage.setdefault(year, {}).setdefault(month, {}).setdefault('total', 0)
    result_summ = storage[year][month]['total']

    return f"Расход за {month} месяц {year} года составляет {result_summ}"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    global storage
    storage.setdefault(year, {}).setdefault('total', 0)
    result_summ = storage[year]['total']

    return f"Расход за {year} год составляет {result_summ}"


if __name__ == "__main__":
    app.run(debug=True)

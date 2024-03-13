from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:elements>")
def max_numm(elements: str):
    elements = elements.split("/")

    nums_list = list()
    for i_elem in elements:
        try:
            nums_list.append(float(i_elem))
        except Exception:
            continue

    max_num = max(nums_list)

    return f"Максимальное число: {max_num}"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:nums>")
def get_max_num(nums: str):
    symbols_list = nums.split("/")
    nums_list = list()

    for num in symbols_list:
        try:
            nums_list.append(float(num))
        except ValueError as error:
            continue
            # print(f"Возникло исклчение, элемент не является цифрой {error}")
        finally:
            if len(nums_list) == 0:
                raise TypeError

    return f"Максимальное число: {max(nums_list)}"


if __name__ == "__main__":
    app.run(debug=True)

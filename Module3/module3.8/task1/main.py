from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/hello/<username>")
def hello_username(username: str):
    day = ("Хорошего понедельника!", "Хорошего вторника!", "Хорошей среды!", "Хорошего четверга!", "Хорошей пятницы!",
           "Хорошей субботы!", "Хорошего воскресенья!")

    if "ошего" in username or "ошей" in username:
        raise ValueError("Имя пользователя не должно содержать пожелания хорошего дня!")

    today_is = datetime.today().weekday()

    return f"Добрый день, {username}. {day[today_is]}"


if __name__ == "__main__":
    app.run(debug=True)

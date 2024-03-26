from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/hello/<username>")
def helo_username(username: str):
    if len(username) > 15 or " " in username:
        raise ValueError("Имя не может быть длинее 15 знаков или содержать проблеы!")

    day = ("Хорошего понедельника!", "Хорошего вторника!", "Хорошей среды!", "Хорошего четверга!", "Хорошей пятницы!",
           "Хорошей субботы!", "Хорошего воскресенья!")

    today_is = datetime.today().weekday()

    return f"Привет, {username}. {day[today_is]}"


if __name__ == "__main__":
    app.run(debug=True)

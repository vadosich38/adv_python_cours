from flask import Flask
from datetime import datetime
import sys

app = Flask(__name__)


@app.route("/hello/<username>")
def hello_world(username: str):
    day = ("Хорошего понедельника!", "Хорошего вторника!", "Хорошей среды!", "Хорошего четерга!", "Хорошей пятницы!",
           "Хорошей субботы!", "Хорошего воскресенья!")

    weekday = datetime.today().weekday()

    return f"Привет, {username}. {day[weekday]}"


if __name__ == "__main__":
    app.run(debug=True)

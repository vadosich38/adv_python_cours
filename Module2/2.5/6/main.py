from flask import Flask
import os

app = Flask(__name__)


@app.route("/preview/<int:size>/<path:file_path>")
def func(size: int, file_path: str):
    abs_path = os.path.abspath(path=file_path)

    with open(file=abs_path, mode="r", encoding="utf-8") as file:
        text = file.read(size)
        text_len = len(text)

    return f"<b>{abs_path}</b> {text_len}<br>{text}"


if __name__ == "__main__":
    app.run(debug=True)

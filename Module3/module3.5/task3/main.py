from flask import Flask
import os

app = Flask(__name__)


@app.route("/file/<path:file_path>")
def work_with_file(file_path: str):

    if not os.path.exists(file_path):
        return "Erorr 404\n\nFile not found", 404

    if ".bin" in file_path:
        raise ValueError

    with open(file=file_path, mode="r", encoding="utf-8") as my_file:
        file_text = my_file.read()
        if file_text == "" or file_text is None:
            return "File is Empty", 200

    return file_text, 200


if __name__ == "__main__":
    app.run(debug=True)

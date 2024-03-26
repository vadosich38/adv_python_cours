import datetime
import random
from flask import Flask
import os
import re

app = Flask('name')

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

with open(BOOK_FILE) as book_file:
    text = book_file.read()
    words_list = re.findall(pattern=r"\b\w+\b", string=text)


@app.route('/cars')
def cars_func():
    return f'{cars[0], cars[1], cars[2], cars[3]}.'


@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'


@app.route('/cats')
def cats_func():
    return f'Рандомная порода: {random.choice(cats)}'


@app.route('/get_time/now')
def time():
    return f'Точное время: {datetime.datetime.now()}'


@app.route('/get_time/future')
def future_time():
    return f'Точное время через час: {datetime.datetime.now() + datetime.timedelta(hours=1)}'


@app.route('/get_random_word')
def random_word():
    return f'Рандомное слово: {random.choice(words_list)}'


@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Страница была открыта: {counter.visits} раз'


counter.visits = 0

if __name__ == "__main__":
    app.run(debug=True)

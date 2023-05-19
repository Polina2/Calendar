# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index/<date>')
def day(date):
    d, m, y = date.split('.')
    months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
      'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
    m = months[int(m)]
    events = []
    return render_template('day.html', day=d, month=m, year=y, events=events)

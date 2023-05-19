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
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
      'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    m = months[int(m)]
    events = []
    return render_template('day.html', month=m, year=y, events=events)

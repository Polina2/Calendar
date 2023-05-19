# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app, db
from app.models import Day, Event


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index/<date>', methods=["POST", "GET"])
def day(date):
    d, m, y = date.split('.')
    params_post = {}
    for p in request.form:
        params_post[p] = request.form[p]

    date_req = '/'.join((d, str(int(m) + 1), y))
    day_req = Day.query.filter(Day.date == date_req).first()
    if 'name' in params_post:
        name = params_post['name']
        if day_req is None:
            new_day = Day(date=date_req)
            db.session.add(new_day)
            db.session.commit()
            day_req = Day.query.filter(Day.date == date_req).first()
        new_event = Event(name=name, day_id=day_req.id)
        if 'time' in params_post:
            time = params_post['time']
            new_event = Event(time=time, name=name, day_id=day_req.id)
        db.session.add(new_event)
        db.session.commit()

    months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
      'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
    m = months[int(m)]
    events = []
    if day_req is not None:
        events = day_req.events
    return render_template('day.html', day=d, month=m, year=y, events=events, date=date)

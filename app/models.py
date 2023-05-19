from app import db


class Day(db.Model):
    __tablename__ = "day"
    id = db.Column("id", db.BigInteger, primary_key=True, autoincrement=True)
    date = db.Column("date", db.Date, nullable=False)
    events = db.relationship('Event', backref='day')


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column("id", db.BigInteger, primary_key=True, autoincrement=True)
    time = db.Column("time", db.Time)
    name = db.Column("name", db.Text, nullable=False)
    day_id = db.Column(db.ForeignKey('day.id'), nullable=False)

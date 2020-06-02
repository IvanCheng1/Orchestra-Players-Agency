import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import datetime

PACKAGE_PARENT = '..'

database_name = "players"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

def add_test_data():
    concert = Concert(
        title = 'Bach returns',
        style = 'Baroque',
        concert_date = '20200101'
    )

    player = Player(
        name = "Austin Pierce",
        instrument = "Violin",
        experience = 3
    )

    player.insert()
    concert.insert()
    db.session.commit()



'''
Concert

'''
class Concert(db.Model):
    __tablename__ = 'concert'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    style = Column(String)
    concert_date = Column(db.DateTime)

    def __init__(self, title, style, concert_date):
        self.title = title
        self.style = style
        self.concert_date = concert_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'style': self.style,
            'concert_date': self.concert_date
        }


'''
Player

'''
class Player(db.Model):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    instrument = Column(String)
    experience = Column(Integer)

    def __init__(self, name, instrument, experience):
        self.name = name
        self.instrument = instrument
        self.experience = experience

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'instrument': self.instrument,
            'experience': str(self.experience) + ' year(s)'
        }

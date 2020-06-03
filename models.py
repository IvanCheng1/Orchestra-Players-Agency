import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import datetime
from flask_migrate import Migrate, MigrateCommand


database_name = "players"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path_local = "postgres://{}/{}".format(
    'localhost:5432', database_name)
database_path = os.environ.get('DATABASE_URL', database_path_local)

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
        title='Bach returns',
        style='Baroque',
        concert_date='20200101'
    )

    concert2 = Concert(
        title='Mozart returns',
        style='Classical',
        concert_date='20220101'
    )

    player = Player(
        name="Austin Pierce",
        instrument="Violin",
        experience=3
    )

    player2 = Player(
        name="Harry Potter",
        instrument="Broom",
        experience=2
    )

    orchestra = Orchestra(
        concert_id=1,
        player_id=1
    )

    player.insert()
    player2.insert()
    concert.insert()
    concert2.insert()
    orchestra.insert()
    db.session.commit()


#----------------------------------------------------------------------------#
# Concert
#----------------------------------------------------------------------------#
class Concert(db.Model):
    __tablename__ = 'concert'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    style = Column(String)
    concert_date = Column(db.DateTime)
    orchestra = db.relationship(
        "Orchestra", backref="concert", passive_deletes=True, lazy=True)

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
            'concert_date': self.concert_date,
            'players_booked': Orchestra.query.filter(Orchestra.concert_id == self.id).count()
        }


#----------------------------------------------------------------------------#
# Player
#----------------------------------------------------------------------------#
class Player(db.Model):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    instrument = Column(String)
    experience = Column(Integer)
    orchestra = db.relationship(
        "Orchestra", backref="player", passive_deletes=True, lazy=True)

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
            'experience': str(self.experience) + ' year(s)',
            'concerts_booked': Orchestra.query.filter(Orchestra.player_id == self.id).count()
        }

#----------------------------------------------------------------------------#
# Orchestra (association table)
#----------------------------------------------------------------------------#


class Orchestra(db.Model):
    __tablename__ = 'orchestra'

    id = db.Column(db.Integer, primary_key=True)
    concert_id = db.Column(db.Integer, db.ForeignKey(
        'concert.id', ondelete='CASCADE'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey(
        'player.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, concert_id, player_id):
        self.concert_id = concert_id
        self.player_id = player_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"concert_id:  {self.concert_id}\n"
                f"player_id:   {self.player_id}")

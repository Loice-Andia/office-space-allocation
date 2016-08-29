from app.amity import my_amity
from app.amity.amityClass import rooms
from app.person.personClass import people_data
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, Integer, String, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database(object):
    """ Database class"""

    def __init__(self):
        self.db = None
        self.amity = my_amity

    def save_state(self, args):
        """
        Takes up an optional argument --db that specifies the
        database to store the data in rooms and people dictionary.
        Creates database and saves data.
        """
        print args
        if args["--db"]:
            self.db_name = args["--db"]
        else:
            self.db_name = "amity.db"
        self.db = create_engine("sqlite:///" + self.db_name)
        print "Data has been stored in the "
        print self.db_name + " database"

    def load_state(self, args):
        """
        Loads data from a database into the application
        """
        print args

class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    room_type = Column(String)
    occupants_id = Column(Integer, ForeignKey('people.id'))
    occupants = relationship(
        'people',
        secondary='department_employee_link'
    )

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_staff = Column(Boolean)
    

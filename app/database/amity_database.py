from app.amity import my_amity
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table


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

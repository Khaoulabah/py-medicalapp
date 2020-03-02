import pymysql.cursors
import queries
import api
from database import Database
from api import API

# Connect to the database
try:
    db = Database()
    api = API(db)
    api.getEmployees()
finally:
    db.connection.close()

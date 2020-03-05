import pymysql.cursors
import queries
import api
from database import Database
from api import API

# Connect to the database
try:
    db = Database()
    api = API(db)
    # correct
    api.getPatients()
    # correct
    api.getPatientId('Benedict', 'Tyson')
    # correct
    api.getMedicalStaff()
    # correct
    api.getMedicalStaffId('Abdul', 'Heath')
    # correct
    api.getAppointments()
finally:
    db.connection.close()

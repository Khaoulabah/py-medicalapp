import queries


class API:
    def __init__(self, db):
        self.db = db

    def getEmployees(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_EMPLOYEES)
            for row in cursor:
                print(row)

    def getPatientContactInfo(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_CONTACTINFO, (patientId))
            for row in cursor:
                print(row)

    def getNotesForAllAppointments(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_NOTES_FOR_ALL_APPOINTMENTS, (patientId))
            for row in cursor:
                print(row)
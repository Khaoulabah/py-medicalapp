import queries


class API:
    def __init__(self, db):
        self.db = db

    def getEmployees(self):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_EMPLOYEES)
            for row in cursor:
                print(row)

    def getPatientContactInfo(self, patientId):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_CONTACTINFO, (patientId))
            for row in cursor:
                print(row)

    def getPatientNotes(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_NOTES, (firstName, lastName))
            for row in cursor:
                print(row)

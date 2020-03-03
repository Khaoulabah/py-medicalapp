import queries


class API:
    def __init__(self, db):
        self.db = db

    def getPatientId(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_ID, (firstName, lastName))
            for row in cursor:
                print(row)

    def getMedicalStaffId(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_MEDICAL_STAFF_ID, (firstName, lastName))
            for row in cursor:
                print(row)

    def getMedicalStaff(self):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_MEDICAL_STAFF)
            for row in cursor:
                print(row)

    def getPatients(self):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENTS)
            for row in cursor:
                print(row)

    def getPatientContactInfo(self, patientId):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_CONTACTINFO, (patientId))
            for row in cursor:
                print(row)

    def getPatientNotes(self, patientId):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_NOTES, (patientId))
            for row in cursor:
                print(row)

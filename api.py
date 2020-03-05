import queries
import crud


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

    def getAppointments(self):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_APPOINTMENTS)
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
            cursor.execute(queries.GET_PATIENT_CONTACTINFO, (patientId))
            for row in cursor:
                print(row)

    def getNotesForAllAppointments(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_NOTES_FOR_ALL_APPOINTMENTS, (patientId))
            for row in cursor:
                print(row)

    def getPatientNotes(self, patientId):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_NOTES % (patientId))
            for row in cursor:
                print(row)

    def getPatientConditions(self, patientId):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_PATIENT_CONDITIONS, (patientId))
            for row in cursor:
                print(row)

    def getAppointmentsBetween(self, startTime, endTime):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime))
            for row in cursor:
                print(row)

    def getAvailableStaff(self, startTime, endTime):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_AVAILABLE_STAFF, (startTime, endTime))
            for row in cursor:
                print(row)

    def getAppointmentStaff(self, appointmentId):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_APPOINTMENT_STAFF, (appointmentId))
            for row in cursor:
                print(row)

    def addPatient(self, FirstName, LastName, Gender, DateOfBirth, Weight, Height):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_PATIENT, (FirstName, LastName, Gender, DateOfBirth, Weight, Height))

    def updateWeight(self, PatientID, Weight):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_WEIGHT, (Weight, PatientID))

    def updateHeight(self, PatientID, Height):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_HEIGHT, (Height, PatientID))

    def updatePhoneNumber(self, PhoneInfoID, PhoneNumber):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_PHONENUMBER, (PhoneNumber, PhoneInfoID))

    def updateAddress(self, PatientID, StreetAddress, AppNumber, City, State, ZipCode):
            with self.db.connection.cursor() as cursor:
                cursor.execute(crud.UPDATE_ADDRESS, (StreetAddress, AppNumber, City, State, ZipCode))

    def updateNote(self, AppointmentID, AuthorID, Content):
            with self.db.connection.cursor() as cursor:
                cursor.execute(crud.UPDATE_NOTE, (Content, AuthorID, AppointmentID))

    def addMedicalCondition(self, PatientID, ConditionInfo, Status):
            with self.db.connection.cursor() as cursor:
                cursor.execute(crud.ADD_MEDICAL_DIAGNOSIS, (PatientID, ConditionInfo, Status))

    def updateMedicalDiagnosisConditionInfo(self, MedicalDiagnosisID, ConditionInfo):
            with self.db.connection.cursor() as cursor:
                cursor.execute(crud.UPDATE_MEDICAL_DIAGNOSIS_CONDITIONINFO, (ConditionInfo, MedicalDiagnosisID))

    def updateMedicalDiagnosisStatus(self, MedicalDiagnosisID, Status):
            with self.db.connection.cursor() as cursor:
                cursor.execute(crud.UPDATE_MEDICAL_DIAGNOSIS_Status, (Status, MedicalDiagnosisID))

    def createNewAppointment(self,PatientID, RoomID, Date, Duration, PurposeID, MedicalStaffID):
             with self.db.connection.cursor() as cursor:
                cursor.execute(crud.CREATE_NEW_APPOINTMENT, (PatientID, RoomID, Date, Duration, PurposeID, MedicalStaffID))

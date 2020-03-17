import queries
import crud


class API:
    def __init__(self, db):
        self.db = db

    def getPatientId(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_ID, (firstName, lastName))
            for row in cursor:
                print(row)

    def getMedicalStaffId(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_MEDICAL_STAFF_ID, (firstName, lastName))
            for row in cursor:
                print(row)

    def getMedicalStaff(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_MEDICAL_STAFF)
            for row in cursor:
                print(row)

    def getAppointments(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS)
            for row in cursor:
                print(row)

    # Working
    def getAppointmentsForPatient(self, PatientID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_FOR_PATIENT, (PatientID))
            for row in cursor:
                print(row)

    def getPatients(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENTS)
            columns = tuple(column[0] for column in cursor.description)
            print(columns)
            for row in cursor:
                print(row)

    def getPatientContactInfo(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_CONTACT_INFO, (patientId))
            for row in cursor:
                print(row)

    # Working
    def getPatientNotes(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_NOTES, (patientId))
            for row in cursor:
                print(row)

    # Working
    def getPatientConditions(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_CONDITIONS, (patientId))
            for row in cursor:
                print(row)

    def getAppointmentsBetween(self, startTime, endTime):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime))
            for row in cursor:
                print(row)

    def getAvailableStaff(self, startTime, endTime):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_AVAILABLE_STAFF, (startTime, endTime))
            for row in cursor:
                print(row)

    def getAppointmentsBetweenByPatientID(self, startTime, endTime, patientID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime, patientID))
            for row in cursor:
                print(row)

    def getAppointmentsBetweenByStaffID(self, startTime, endTime, staffID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime, staffID))
            for row in cursor:
                print(row)

    # Working
    def getMedicalStaffForAppointment(self, AppointmentID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_STAFF_FOR_APPOINTMENT, (AppointmentID))
            for row in cursor:
                print(row)

    # Working
    def deleteAppointment(self, appointmentId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(
                crud.DELETE_ALL_STAFF_FOR_APPOINTMENT, (appointmentId))
            cursor.execute(crud.DELETE_APPOINTMENT, (appointmentId))

    # Working
    def rescheduleAppointment(self, appointmentId, newDate):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.RESCHEDULE_APPOINTMENT,
                           (newDate, appointmentId))

    # Working but not finished yet. Needs ADD_PHONE_NUMBER
    def addPatient(self, FirstName, LastName, Gender, DateOfBirth, Weight, Height, StreetAddress, City, State, ZipCode, AppNumber):
        with self.db.connection.cursor() as cursor:
            if AppNumber == '':
                AppNumber = None
            cursor.execute(crud.ADD_ADDRESS, (StreetAddress,
                                              City, State, ZipCode, AppNumber))
            cursor.execute(crud.ADD_PATIENT, (FirstName, LastName,
                                              Gender, DateOfBirth, Weight, Height, cursor.lastrowid))

    # Working
    def updateWeight(self, PatientID, Weight):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_WEIGHT, (Weight, PatientID))

    # Working
    def updateHeight(self, PatientID, Height):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_HEIGHT, (Height, PatientID))

    # Not tested need to get phoneinfoId
    def updatePhoneNumber(self, PhoneInfoID, PhoneNumber):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_PHONENUMBER, (PhoneNumber, PhoneInfoID))

    # Working
    def updateAddress(self, PatientID, StreetAddress, AppNumber, City, State, ZipCode):
        if AppNumber == '':
            AppNumber = None
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_ADDRESS, (StreetAddress,
                                                 AppNumber, City, State, ZipCode, PatientID))

    # Working
    def addNote(self, AppointmentID, AuthorID, Content):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_NOTE, (AuthorID, AppointmentID, Content))

    # Working
    def updateNote(self, AppointmentID, AuthorID, Content):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_NOTE,
                           (Content, AuthorID, AppointmentID))

    # Working
    def deleteNote(self, AppointmentID, AuthorID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.DELETE_NOTE, (AuthorID, AppointmentID))

    # Working
    def addMedicalDiagnosis(self, PatientID, ConditionInfo, Status):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_MEDICAL_DIAGNOSIS,
                           (PatientID, ConditionInfo, Status))

    # Working
    def updateMedicalDiagnosisConditionInfo(self, MedicalDiagnosisID, ConditionInfo):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_MEDICAL_DIAGNOSIS_CONDITIONINFO,
                           (ConditionInfo, MedicalDiagnosisID))

    # Working
    def updateMedicalDiagnosisStatus(self, MedicalDiagnosisID, Status):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_MEDICAL_DIAGNOSIS_STATUS,
                           (Status, MedicalDiagnosisID))

    # Working
    def createNewAppointment(self, PatientID, RoomID, Date, Duration, PurposeID, MedicalStaffID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.CREATE_NEW_APPOINTMENT,
                           (PatientID, RoomID, Date, Duration, PurposeID))
            cursor.execute(crud.ADD_STAFF_FOR_APPOINTMENT,
                           (MedicalStaffID, cursor.lastrowid))

    # Working
    def addStaffForAppointment(self, MedicalStaffID, AppointmentID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_STAFF_FOR_APPOINTMENT,
                           (MedicalStaffID, AppointmentID))

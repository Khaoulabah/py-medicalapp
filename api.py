import queries
import crud
from prettytable import *


class API:
    def __init__(self, db):
        self.db = db

    # Working
    def getPatientId(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_ID, (firstName, lastName))
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getMedicalStaffId(self, firstName, lastName):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_MEDICAL_STAFF_ID, (firstName, lastName))
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getMedicalStaff(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_MEDICAL_STAFF)
            table = from_db_cursor(cursor)
            print(table)

    def getAppointments(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS)
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getAppointmentsForPatient(self, PatientID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_FOR_PATIENT, (PatientID))
            table = from_db_cursor(cursor)
            print(table)

    def getPatients(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENTS)
            table = from_db_cursor(cursor)
            print(table)

    def getPatientContactInfo(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_CONTACT_INFO, (patientId))
            table = from_db_cursor(cursor)
            print(table)

    def getPatientMedicalInfo(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_MEDICAL_INFO, (patientId))
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getPatientNotes(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_NOTES, (patientId))
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getPatientConditions(self, patientId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PATIENT_CONDITIONS, (patientId))
            table = from_db_cursor(cursor)
            print(table)

    def getAppointmentsBetween(self, startTime, endTime):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime))
            table = from_db_cursor(cursor)
            print(table)

    def getAvailableStaff(self, startTime, endTime):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_AVAILABLE_STAFF, (startTime, endTime))
            table = from_db_cursor(cursor)
            print(table)

    def getAppointmentsBetweenByPatientID(self, startTime, endTime, patientID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime, patientID))
            table = from_db_cursor(cursor)
            print(table)

    def getAppointmentsBetweenByStaffID(self, startTime, endTime, staffID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_APPOINTMENTS_BETWEEN,
                           (startTime, endTime, staffID))
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getMedicalStaffForAppointment(self, AppointmentID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_STAFF_FOR_APPOINTMENT, (AppointmentID))
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getRooms(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_ROOMS)
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def getPurposes(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(queries.GET_PURPOSES)
            table = from_db_cursor(cursor)
            print(table)

    # Working
    def deleteAppointment(self, appointmentId):
        with self.db.connection.cursor() as cursor:
            cursor.execute(
                crud.DELETE_ALL_STAFF_FOR_APPOINTMENT, (appointmentId))
            cursor.execute(crud.DELETE_APPOINTMENT, (appointmentId))
            self.db.connection.commit()

    # Working
    def rescheduleAppointment(self, appointmentId, newDate):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.RESCHEDULE_APPOINTMENT,
                           (newDate, appointmentId))
            self.db.connection.commit()

    # Working but not finished yet. Needs ADD_PHONE_NUMBER
    def addPatient(self, FirstName, LastName, Gender, DateOfBirth, Weight, Height, StreetAddress, City, State, ZipCode, AppNumber, Number, PhoneType):
        with self.db.connection.cursor() as cursor:
            if AppNumber == '':
                AppNumber = None
            cursor.execute(crud.ADD_ADDRESS, (StreetAddress,
                                              City, State, ZipCode, AppNumber))
            cursor.execute(crud.ADD_PATIENT, (FirstName, LastName,
                                              Gender, DateOfBirth, Weight, Height, cursor.lastrowid))
            cursor.execute(
                crud.ADD_PHONE, (cursor.lastrowid, None, PhoneType, Number))
            self.db.connection.commit()

    # Working
    def updateWeight(self, PatientID, Weight):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_WEIGHT, (Weight, PatientID))
            self.db.connection.commit()

    # Working
    def updateHeight(self, PatientID, Height):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_HEIGHT, (Height, PatientID))
            self.db.connection.commit()

    # Not tested need to get phoneinfoId
    def updatePhoneNumber(self, PhoneInfoID, PhoneNumber):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_PHONENUMBER, (PhoneNumber, PhoneInfoID))
            self.db.connection.commit()

    # Working
    def updateAddress(self, PatientID, StreetAddress, AppNumber, City, State, ZipCode):
        if AppNumber == '':
            AppNumber = None
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_ADDRESS, (StreetAddress,
                                                 AppNumber, City, State, ZipCode, PatientID))
            self.db.connection.commit()

    # Working
    def addNote(self, AppointmentID, AuthorID, Content):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_NOTE, (AuthorID, AppointmentID, Content))
            self.db.connection.commit()

    # Working
    def updateNote(self, AppointmentID, AuthorID, Content):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_NOTE,
                           (Content, AuthorID, AppointmentID))
            self.db.connection.commit()

    # Working
    def deleteNote(self, AppointmentID, AuthorID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.DELETE_NOTE, (AuthorID, AppointmentID))
            self.db.connection.commit()

    # Working
    def addMedicalDiagnosis(self, PatientID, ConditionInfo, Status):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_MEDICAL_DIAGNOSIS,
                           (PatientID, ConditionInfo, Status))
            self.db.connection.commit()

    # Working
    def updateMedicalDiagnosisConditionInfo(self, MedicalDiagnosisID, ConditionInfo):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_MEDICAL_DIAGNOSIS_CONDITIONINFO,
                           (ConditionInfo, MedicalDiagnosisID))
            self.db.connection.commit()

    # Working
    def updateMedicalDiagnosisStatus(self, MedicalDiagnosisID, Status):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.UPDATE_MEDICAL_DIAGNOSIS_STATUS,
                           (Status, MedicalDiagnosisID))
            self.db.connection.commit()

    # Working
    def createNewAppointment(self, PatientID, RoomID, Date, Duration, PurposeID, MedicalStaffID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.CREATE_NEW_APPOINTMENT,
                           (PatientID, RoomID, Date, Duration, PurposeID))
            cursor.execute(crud.ADD_STAFF_FOR_APPOINTMENT,
                           (MedicalStaffID, cursor.lastrowid))
            self.db.connection.commit()

    # Working

    def addStaffForAppointment(self, AppointmentID, MedicalStaffID):
        with self.db.connection.cursor() as cursor:
            cursor.execute(crud.ADD_STAFF_FOR_APPOINTMENT,
                           (MedicalStaffID, AppointmentID))
            self.db.connection.commit()

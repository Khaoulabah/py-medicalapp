import pymysql.cursors
import queries
import api
from database import Database
from api import API

# Connect to the database
try:
    db = Database()
    api = API(db)

    calls = [
        {
            'name': "Get Patients",
            'function': api.getPatients,
            'parameters': []
        },
        {
            'name': "Get Patient Information",
            'function': api.getPatientContactInfo,
            'parameters': [
                'patientId'
            ]
        },
        {
            'name': "Add Patient",
            'function': api.addPatient,
            'parameters': [
                'FirstName', 'LastName', 'Gender', 'DateOfBirth', 'Weight', 'Height'
            ]
        },
        {
            'name': "Update Patient Weight",
            'function': api.updateWeight,
            'parameters': [
                'PatientID', 'Weight'
            ]
        },
        {
            'name': "Update Patient Height",
            'function': api.updateHeight,
            'parameters': [
                'PatientID', 'Height'
            ]
        },
        {
            'name': "Update Patient Phone Number",
            'function': api.updatePhoneNumber,
            'parameters': [
                'PhoneInfoID', 'PhoneNumber'
            ]
        },
        {
            'name': "Update Patient Address",
            'function': api.updateAddress,
            'parameters': [
                'PatientID', 'StreetAddress', 'AppNumber', 'City', 'State', 'ZipCode'
            ]
        },
        {
            'name': "Add Note",
            'function': api.addNote,
            'parameters': [
                'AppointmentID', 'AuthorID', 'Content'
            ]
        },
        {
            'name': "Update Note",
            'function': api.updateNote,
            'parameters': [
                'AppointmentID', 'AuthorID', 'Content'
            ]
        },
        {
            'name': "Delete Note",
            'function': api.deleteNote,
            'parameters': [
                'AppointmentID', 'AuthorID'
            ]
        },
        {
            'name': "Add Medical Diagnosis",
            'function': api.addMedicalDiagnosis,
            'parameters': [
                'PatientID', 'ConditionInfo', 'Status'
            ]
        },
        {
            'name': "Update Condition Information about Medical Diagnosis",
            'function': api.updateMedicalDiagnosisConditionInfo,
            'parameters': [
                 'MedicalDiagnosisID', 'ConditionInfo'
            ]
        },
        {
            'name': "Update Status of Medical Diagnosis",
            'function': api.updateMedicalDiagnosisStatus,
            'parameters': [
                'MedicalDiagnosisID', 'Status'
            ]
        },
        {
            'name': "Create New Appointment",
            'function': api.createNewAppointment,
            'parameters': [
                'PatientID', 'RoomID', 'Date', 'Duration', 'PurposeID', 'MedicalStaffID'
            ]
        }
    ]

    running = True
    while running:
        for i in range(len(calls)):
            print('{}. '.format(i + 1) + calls[i]['name'])

        ui = int(input('Choose an option (type -1 to quit): '))
        if ui == -1:
            running = False
            break
        while ui < 1 or ui > len(calls):
            if (ui = int(input('Invalid Choice (type -1 to quit): '))) == -1:
                break

        currentCall = calls[ui - 1]
        parameters = []
        for i in range(len(currentCall['parameters'])):
            parameters.append(input(
                'Please enter, ' + currentCall['parameters'][i] + ': '))

        calls[ui - 1]['function'](*parameters)

finally:
    db.connection.close()

import pymysql.cursors
import queries
import api
from database import Database
from api import API


def printCalls(callList):
    running = True
    while running:
        for i in range(len(callList)):
            print('{}. '.format(i + 1) + callList[i]['name'])

        ui = int(
            input('Choose an option (0 to go back to category menu, -1 to quit): '))
        if ui <= -1:
            running = False
            return False
        if ui == 0:
            running = False
            return True
        if ui > len(callList):
            print('Invalid Choice (type -1 to quit): ')

        currentCall = callList[ui - 1]
        parameters = []
        for i in range(len(currentCall['parameters'])):
            parameters.append(
                input('Please enter, ' + currentCall['parameters'][i] + ': '))

        callList[ui - 1]['function'](*parameters)


# Connect to the database
try:
    db = Database()
    api = API(db)

    create = [
        {
            'name': "Add Patient",
            'function': api.addPatient,
            'parameters': [
                'FirstName', 'LastName', 'Gender', 'DateOfBirth', 'Weight', 'Height'
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
            'name': "Add Medical Diagnosis",
            'function': api.addMedicalDiagnosis,
            'parameters': [
                'PatientID', 'ConditionInfo', 'Status'
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

    update = [
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
            'name': "Update Note",
            'function': api.updateNote,
            'parameters': [
                'AppointmentID', 'AuthorID', 'Content'
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
        }
    ]

    remove = [
        {
            'name': "Delete Note",
            'function': api.deleteNote,
            'parameters': [
                'AppointmentID', 'AuthorID'
            ]
        },
    ]

    retrieve = [
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
    ]

    running = True
    while running:
        print("""1. Retreival\n2. Update\n3. Create\n4. Remove""")
        ui = int(input('Choose a category (-1 to quit): '))
        if ui <= -1:
            running = False
            break
        if ui > 4:
            print('Invalid option, choose 1-4 or -1 to quit.')
        if ui == 1:
            running = printCalls(retrieve)
        elif ui == 2:
            running = printCalls(update)
        elif ui == 3:
            running = printCalls(create)
        elif ui == 4:
            running = printCalls(remove)

finally:
    db.connection.close()

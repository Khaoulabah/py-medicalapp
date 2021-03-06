import queries
import api
from database import Database
from api import API
from pyfiglet import Figlet
from pyfiglet import print_figlet
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        # system('cls')
        pass
    # for mac and linux(here, os.name is 'posix')
    else:
        # system('clear')
        pass


def printCalls(callList):
    running = True
    while running:
        for i in range(len(callList)):
            print('{}. '.format(i + 1) + callList[i]['name'])
        try:
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
                running = True
                continue

            currentCall = callList[ui - 1]
            parameters = []
            for i in range(len(currentCall['parameters'])):
                parInput = input('Please enter, ' +
                                 currentCall['parameters'][i] + ': ')
                parameters.append(parInput)

            callList[ui - 1]['function'](*parameters)
            print()
        except ValueError:
            print()
            print("Only numbers are accepted for this menu. Please try again")
            print()


# Clear screen and show loading text
clear()
print_figlet("Connecting...", font='big', colors="RESET")

# Connect to the database
try:
    db = Database()
    api = API(db)
    clear()
    print_figlet("Connected!", font='big', colors="GREEN")
    sleep(0.5)

    create = [
        {
            'name': "Add Patient",
            'function': api.addPatient,
            'parameters': [
                'FirstName',
                'LastName',
                'Gender (Male/Female)',
                'DateOfBirth (YYYY-MM-DD)',
                'Weight (lbs)',
                'Height (in.)',
                'StreetAddress',
                'City',
                'State',
                'ZipCode',
                'AppartmentNUmber (optional)',
                'PhoneNumber',
                'PhoneType (C/W/H)'
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
                'PatientID', 'RoomID', 'Date and Time (YYYY-MM-DD HH:MM:SS)', 'Duration (Min)', 'PurposeID', 'MedicalStaffID'
            ]
        },
        {
            'name': "Add Medical Staff to Appointment",
            'function': api.addStaffForAppointment,
            'parameters': [
                'AppointmentID', 'MedicalStaffID']
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
        },
        {
            'name': "Reschedule Appointment",
            'function': api.rescheduleAppointment,
            'parameters': [
                'appointmentId', 'newDate'
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
        {
            'name': "Cancel Appointment",
            'function': api.deleteAppointment,
            'parameters': [
                'AppointmentID'
            ]
        },
    ]

    retrieve = [
        {
            'name': "Get All Patients",
            'function': api.getPatients,
            'parameters': []
        },
        {
            'name': "Get PatientID",
            'function': api.getPatientId,
            'parameters': ['FirstName', 'LastName']
        },
        {
            'name': "Get Patient's Contact Information",
            'function': api.getPatientContactInfo,
            'parameters': [
                'PatientID'
            ]
        },
        {
            'name': "Get Patient's Medical Information",
            'function': api.getPatientMedicalInfo,
            'parameters': [
                'PatientID'
            ]
        },
        {
            'name': "Get All Notes for a Patient",
            'function': api.getPatientNotes,
            'parameters': ['patientId']
        },
        {
            'name': "Get Patient Appointments",
            'function': api.getAppointmentsForPatient,
            'parameters': [
                'PatientID'
            ]
        },
        {
            'name': "Get Medical Conditions of a Patient",
            'function': api.getPatientConditions,
            'parameters': ['patientId']
        },
        {
            'name': "Get All Medical Staff",
            'function': api.getMedicalStaff,
            'parameters': []
        },
        {
            'name': "Get Medical Staff ID",
            'function': api.getMedicalStaffId,
            'parameters': ['FirstName', 'LastName']
        },
        {
            'name': "Get All Appointments",
            'function': api.getAppointments,
            'parameters': []
        },
        {
            'name': "Get Medical Staff for an Appointment",
            'function': api.getMedicalStaffForAppointment,
            'parameters': [
                'AppointmentID'
            ]
        },
        {
            'name': "Get All Rooms",
            'function': api.getRooms,
            'parameters': []
        },
        {
            'name': "Get All Purposes",
            'function': api.getPurposes,
            'parameters': []
        },
    ]

    running = True
    while running:
        clear()
        print_figlet("Categories:", font='big', colors="CYAN")
        print("""1. Retrieval\n2. Update\n3. Create\n4. Remove""")
        try:
            ui = int(input('Choose a category (-1 to quit): '))
            if ui <= -1:
                running = False
                break
            if ui > 4:
                print('Invalid option, choose 1-4 or -1 to quit.')
            if ui == 1:
                clear()
                print_figlet("Retrievals:", font='big', colors="CYAN")
                running = printCalls(retrieve)
            elif ui == 2:
                clear()
                print_figlet("Updates:", font='big', colors="CYAN")
                running = printCalls(update)
            elif ui == 3:
                clear()
                print_figlet("Inserts:", font='big', colors="CYAN")
                running = printCalls(create)
            elif ui == 4:
                clear()
                print_figlet("Removals:", font='big', colors="CYAN")
                running = printCalls(remove)
        except ValueError:
            print()
            print(
                "Only numbers are accepted for this menu.")
            input("Press ENTER to try again")

finally:
    db.connection.close()

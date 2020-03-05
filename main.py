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
        }
    ]

    for i in range(len(calls)):
        print('{}. '.format(i + 1) + calls[i]['name'])

    ui = int(input('Choose an option: '))
    currentCall = calls[ui - 1]
    parameters = []
    for i in range(len(currentCall['parameters'])):
        parameters.append(input(
            'Please enter, ' + currentCall['parameters'][i] + ': '))

    print(*parameters)
    calls[ui - 1]['function'](*parameters)
finally:
    db.connection.close()

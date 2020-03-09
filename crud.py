ADD_PATIENT = '''
                INSERT INTO Patient (FirstName, LastName, Gender, DateOfBirth, Weight, Height, AddressID)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            '''

ADD_ADDRESS_NO_APPT = '''
                INSERT INTO Address (StreetAddress, City, State, ZipCode)
                VALUES (%s, %s, %s, %s);
            '''

ADD_ADDRESS_WITH_APPT = '''
                INSERT INTO Address (StreetAddress, City, State, ZipCode, AppNumber)
                VALUES (%s, %s, %s, %s, %s);
            '''

GET_INSERT_ID = '''SELECT LAST_INSERT_ID() AS ID'''

UPDATE_WEIGHT = '''
                UPDATE Patient
                SET Weight = %s
                WHERE ID = %s
            '''

UPDATE_HEIGHT = '''
                UPDATE Patient
                SET Height = %s
                WHERE ID = %s
            '''

UPDATE_PHONENUMBER = '''
                UPDATE PhoneInfo
                SET Number = %s
                WHERE ID = %s
            '''

UPDATE_ADDRESS = '''
                UPDATE Address
                SET StreetAddress = %s, AppNumber = %s, City = %s, State = %s, ZipCode = %s
                WHERE ID = %s
            '''

ADD_NOTE = '''
                INSERT INTO Note (AuthorID, AppointmentID, Content, Date)
                VALUES(%s, %s, %s,  NOW())
            '''

UPDATE_NOTE = '''
                UPDATE Note
                SET Content = %s, Date = NOW()
                WHERE AuthorID = %s and AppointmentID = %s
            '''

DELETE_NOTE = '''
                DELETE FROM Note
                WHERE AuthorID = %s and AppointmentID = %s
            '''

ADD_MEDICAL_DIAGNOSIS = '''
                        INSERT INTO MedicalDiagnosis (PatientID, ConditionInfo, Status, Date)
                        VALUES (%s, %s, %s, NOW())
                        '''

UPDATE_MEDICAL_DIAGNOSIS_CONDITIONINFO = '''
                            UPDATE MedicalDiagnosis
                            SET ConditionInfo = %s, Date = NOW()
                            WHERE ID = %s
                            '''

UPDATE_MEDICAL_DIAGNOSIS_STATUS = '''
                            UPDATE MedicalDiagnosis
                            SET Status = %s, Date = NOW()
                            WHERE ID = %s
                            '''

CREATE_NEW_APPOINTMENT = '''
                        INSERT INTO Appointment (PatientID, RoomID, Date, Duration, PurposeID)
                        VALUES (%s, %s, %s, %s, %s);
                        INSERT INTO StaffForAppointment (MedicalStaffID, AppointmentID)
                        VALUES (%s, LAST_INSERT_ID())
                        '''

DELETE_APPOINTMENT = '''
                        DELETE FROM Appointment WHERE Appointment.ID = %s;
                    '''

RESCHEDULE_APPOINTMENT = '''
                            UPDATE Appointment
                            SET date = %s
                            WHERE Appointment.ID = %s
                        '''

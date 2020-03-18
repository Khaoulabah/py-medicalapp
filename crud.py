ADD_PATIENT = '''
                INSERT INTO Patient (FirstName, LastName, Gender, DateOfBirth, Weight, Height, AddressID)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            '''

ADD_ADDRESS = '''
                INSERT INTO Address (StreetAddress, City, State, ZipCode, AppNumber)
                VALUES (%s, %s, %s, %s, %s);
            '''

ADD_PHONE = '''
                INSERT INTO PhoneInfo (PatientId, StaffID, TypeID, Number)
                VALUES (%s, %s, %s, %s);
            '''


#Working
UPDATE_WEIGHT = '''
                UPDATE Patient
                SET Weight = %s
                WHERE ID = %s
            '''

#Working
UPDATE_HEIGHT = '''
                UPDATE Patient
                SET Height = %s
                WHERE ID = %s
            '''

#Not tested
UPDATE_PHONENUMBER = '''
                UPDATE PhoneInfo
                SET Number = %s
                WHERE ID = %s
            '''
#not working when apptmentNum is not provided
UPDATE_ADDRESS = '''
                UPDATE Address
                SET StreetAddress = %s, AppNumber = %s, City = %s, State = %s, ZipCode = %s
                WHERE ID IN (
                    SELECT AddressID
                    FROM Patient
                    WHERE ID = %s
                )
            '''
#working
ADD_NOTE = '''
                INSERT INTO Note (AuthorID, AppointmentID, Content, Date)
                VALUES(%s, %s, %s,  NOW())
            '''

#Working
UPDATE_NOTE = '''
                UPDATE Note
                SET Content = %s, Date = NOW()
                WHERE AuthorID = %s and AppointmentID = %s
            '''

#Working
DELETE_NOTE = '''
                DELETE FROM Note
                WHERE AuthorID = %s and AppointmentID = %s
            '''

#Working
ADD_MEDICAL_DIAGNOSIS = '''
                        INSERT INTO MedicalDiagnosis (PatientID, ConditionInfo, Status, Date)
                        VALUES (%s, %s, %s, NOW())
                        '''

#Working
UPDATE_MEDICAL_DIAGNOSIS_CONDITIONINFO = '''
                            UPDATE MedicalDiagnosis
                            SET ConditionInfo = %s, Date = NOW()
                            WHERE ID = %s
                            '''

#Working
UPDATE_MEDICAL_DIAGNOSIS_STATUS = '''
                            UPDATE MedicalDiagnosis
                            SET Status = %s, Date = NOW()
                            WHERE ID = %s
                            '''

#Working
CREATE_NEW_APPOINTMENT = '''
                        INSERT INTO Appointment (PatientID, RoomID, Date, Duration, PurposeID)
                        VALUES (%s, %s, %s, %s, %s);
                        '''

#Working
ADD_STAFF_FOR_APPOINTMENT='''
                           INSERT INTO StaffForAppointment (MedicalStaffID, AppointmentID)
                           VALUES (%s, %s)
                        '''

#Working
DELETE_APPOINTMENT = '''
                        DELETE FROM Appointment
                        WHERE ID = %s;
                    '''

#Working
DELETE_ALL_STAFF_FOR_APPOINTMENT = '''
                                DELETE FROM StaffForAppointment
                                WHERE AppointmentID= %s;
                                '''

#Working
RESCHEDULE_APPOINTMENT = '''
                            UPDATE Appointment
                            SET Date = %s
                            WHERE ID = %s
                        '''

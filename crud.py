ADD_PATIENT = '''
                INSERT INTO Patient (FirstName, LastName, Gender, DateOfBirth, Weight, Height)
                VALUES (%s, %s, %s, %s, %s, %s)
            '''

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

UPDATE_NOTE = '''
                UPDATE Note
                SET Content = %s, Date = NOW()
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

UPDATE_MEDICAL_DIAGNOSIS_Status = '''
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

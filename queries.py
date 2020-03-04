GET_MEDICAL_STAFF = '''
                        SELECT * FROM MedicalStaff;
                    '''
GET_PATIENTS = '''
                    SELECT * FROM Patient;
                '''

GET_PATIENT_NOTES = ''' 
        SELECT N.content AS Content, N.date AS Date, P.purpose AS Purpose, M.LastName AS Author
        FROM Note N
            JOIN MedicalStaff M ON(M.ID = N.AuthorID)
            JOIN Appointment A ON(A.ID = N.AppointmentId)
            JOIN Purpose P ON(P.Id = A.purposeId)
            JOIN Patient PA ON(PA.id = A.patientId)
        WHERE PA.id = %s;
    '''

GET_PATIENT_CONTACTINFO = '''   
                            SELECT FirstName, LastName, Number as PhoneNumber,
                                    Name as PhoneType, StreetAddress, AppNumber, City, State, ZipCode
                                FROM Patient p
                                    JOIN PhoneInfo pi ON (p.ID = pi.personid)
                                    JOIN PhoneType pt ON (pi.typeid= pt.id)
                                    JOIN Address a ON (p.id=a.personid)
                                WHERE p.id = %s;
                            '''
GET_PATIENT_ID = '''
                    SELECT Patient.ID
                    FROM Patient 
                    WHERE Patient.firstName LIKE %s AND Patient.lastName LIKE %s;
                '''

GET_MEDICAL_STAFF_ID = '''
                            SELECT MedicalStaff.ID
                            FROM MedicalStaff
                            WHERE MedicalStaff.firstName LIKE %s AND MedicalStaff.lastName LIKE %s;
                        '''

GET_PATIENT_CONDITIONS = '''
                                SELECT MD.Condition AS Condition, MD.status AS Status, MD.date AS Diagnosis Date 
                                FROM MedicalDiagnosis MD
                                    JOIN Patient P ON(MD.patientId = P.Id) 
                                WHERE p.id = %s;
                            '''

GET_MEDICAL_STAFF = '''
                        SELECT Id, firstName, lastName, email, name
                        FROM MedicalStaff
                            JOIN StaffType ON(StaffType.typeId = MedicalStaff.StaffTypeId)
                    '''
GET_PATIENTS = '''
                    SELECT * FROM Patient
                '''

GET_APPOINTMENTS = '''
                        SELECT * FROM Appointment
                    '''

GET_PATIENT_NOTES = ''' 
        SELECT N.content AS Content, N.date AS Date, P.Name AS Purpose, M.LastName AS Author
        FROM Note N
            JOIN MedicalStaff M ON(M.ID = N.AuthorID)
            JOIN Appointment A ON(A.ID = N.AppointmentId)
            JOIN Purpose P ON(P.Id = A.purposeId)
            JOIN Patient PA ON(PA.id = A.patientId)
        WHERE PA.id = %d
    '''

GET_PATIENT_CONTACTINFO = '''   
                            SELECT FirstName, LastName, Number as PhoneNumber,
                                    Name as PhoneType, StreetAddress, AppNumber, City, State, ZipCode
                                FROM Patient p
                                    JOIN PhoneInfo pi ON (p.ID = p.patientId)
                                    JOIN PhoneType pt ON (pi.typeid= pt.id)
                                    JOIN Address a ON (p.id=a.patientId)
                                WHERE p.id = %s
                            '''
GET_PATIENT_ID = '''
                    SELECT Patient.ID
                    FROM Patient 
                    WHERE Patient.firstName LIKE %s AND Patient.lastName LIKE %s
                '''

GET_MEDICAL_STAFF_ID = '''
                            SELECT MedicalStaff.ID
                            FROM MedicalStaff
                            WHERE MedicalStaff.firstName LIKE %s AND MedicalStaff.lastName LIKE %s
                        '''

GET_PATIENT_CONDITIONS = '''
                                SELECT MD.Condition AS Condition, MD.status AS Status, MD.date AS DiagnosisDate 
                                FROM MedicalDiagnosis MD
                                    JOIN Patient P ON(MD.patientId = P.Id) 
                                WHERE p.id = %s
                            '''

GET_APPOINTMENTS_BETWEEN = '''
                                SELECT ID AS ID, Date AS Date, Duration AS Duration, p.purpose AS Purpose
                                FROM Appointment A
                                    JOIN Purpose P ON(A.purposeId = P.Id)
                                WHERE A.startTime >= %s AND A.startTime <= %s
                            '''
GET_AVAILABLE_STAFF = '''
                            SELECT ID AS ID, firstName AS FirstName, lastName AS LastName
                            FROM MedicalStaff 
                                LEFT JOIN (
                                    SELECT DISTINCT MS.ID AS medicalId
                                    FROM Appointment A
                                        JOIN StaffForAppointment SFA ON(SFA.AppointmentId = A.Id)
                                        JOIN MedicalStaff MS ON(SFA.MedicalStaffId = MS.Id)
                                    WHERE A.date >= %s AND A.date <= %s 
                                ) AS X ON (MedicalStaff.Id = X.medicalId)
                            WHERE X.medicalId IS NULL 
                        '''
GET_APPOINTMENT_STAFF = '''
                                SELECT MS.ID AS ID, MS.firstName AS FirstName, MS.lastName AS LastName, 
                                    ST.name AS Occupation 
                                FROM Appointment A
                                    JOIN StaffForAppointment SFA ON(SFA.appointmentId = A.Id)
                                    JOIN MedicalStaff MS ON(MS.Id = SFA.medicalStaffID)
                                    JOIN StaffType ST ON(ST.typeId = MS.staffTypeId)
                                WHERE Appointment ID LIKE %s
                                '''
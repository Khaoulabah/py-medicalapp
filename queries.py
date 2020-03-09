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

GET_APPOINTMENTS_FOR_PATIENT = '''
                        SELECT * FROM Appointment
                        WHERE PatientID = %s
                    '''

GET_PATIENT_NOTES = '''
        SELECT PA.firstName AS FirstName, PA.lastName LastName, N.content AS Content, N.date AS Date, P.Name AS Purpose, M.LastName AS Author
        FROM Note N
            JOIN MedicalStaff M ON(M.ID = N.AuthorID)
            JOIN Appointment A ON(A.ID = N.AppointmentId)
            JOIN Purpose P ON(P.Id = A.purposeId)
            JOIN Patient PA ON(PA.id = A.patientId)
        WHERE PA.id = %s
    '''
#working
GET_PATIENT_CONTACT_INFO = '''
                            SELECT FirstName, LastName, Number as PhoneNumber,
                                    Name as PhoneType, StreetAddress, AppNumber, City, State, ZipCode
                                FROM Patient p
                                    JOIN PhoneInfo pi ON (p.ID = pi.patientId)
                                    JOIN PhoneType pt ON (pi.typeid = pt.typeid)
                                    JOIN Address a ON (p.addressID=a.Id)
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
                            SELECT *
                            FROM MedicalDiagnosis MD
                            WHERE PatientId = %s
                        '''

GET_APPOINTMENTS_BETWEEN = '''
                                SELECT ID AS ID, Date AS Date, Duration AS Duration, p.purpose AS Purpose
                                FROM Appointment A
                                    JOIN Purpose P ON(A.purposeId = P.Id)
                                WHERE A.Date >= %s AND A.Date <= %s
                            '''
GET_AVAILABLE_STAFF = '''
                            SELECT ID AS ID, firstName AS FirstName, lastName AS LastName
                            FROM MedicalStaff
                                LEFT JOIN (
                                    SELECT DISTINCT MS.ID AS medicalId
                                    FROM Appointment A
                                        JOIN StaffForAppointment SFA ON(SFA.AppointmentId = A.Id)
                                        JOIN MedicalStaff MS ON(SFA.MedicalStaffId = MS.Id)
                                    WHERE A.Date <= %s AND A.Date >= %s
                                ) AS X ON (MedicalStaff.Id = X.medicalId)
                            WHERE X.medicalId IS NULL
                        '''

GET_APPOINTMENTS_BETWEEN_PATIENTID = '''
                                SELECT ID AS ID, Date AS Date, Duration AS Duration, p.purpose AS Purpose, T.FirstName AS FirstName, T.LastName AS LastName
                                FROM Appointment A
                                    JOIN Purpose P ON(A.purposeId = P.Id)
                                    JOIN Patient T ON(A.PatientID = T.ID)
                                WHERE A.Date >= %s AND A.Date <= %s AND T.ID = %s
                            '''

GET_APPOINTMENTS_BETWEEN_STAFFID = '''
                                SELECT ID AS ID, Date AS Date, Duration AS Duration, p.purpose AS Purpose, M.FirstName AS FirstName, M.LastName AS LastName
                                FROM Appointment A
                                    JOIN Purpose P ON(A.purposeId = P.Id)
                                    JOIN StaffForAppointment T ON(T.AppointmentID = A.ID)
                                    JOIN MedicalStaff M ON(T.MedicalStaffID = M.ID)
                                WHERE A.Date >= %s AND A.Date <= %s AND M.ID = %s
                            '''

#Working
GET_STAFF_FOR_APPOINTMENT = '''
                            SELECT FirstName, LastName, ST.Name as Role
                            FROM MedicalStaff M
                                JOIN StaffForAppointment T ON (T.MedicalStaffID = M.ID)
                                JOIN StaffType ST ON (ST.TypeID = M.StaffTypeId)
                            WHERE T.AppointmentID = %s
                            '''

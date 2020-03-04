GET_EMPLOYEES = '''SELECT * FROM Employees'''

GET_PATIENT_CONTACTINFO = '''   SELECT FirstName, LastName, Number as PhoneNumber,
                                    Name as PhoneType, StreetAddress, AppNumber, City, State, ZipCode
                                FROM Patient p
                                    JOIN PhoneInfo pi ON (p.ID = pi.personid)
                                    JOIN PhoneType pt ON (pi.typeid= pt.id)
                                    JOIN Address a ON (p.id=a.personid)
                                WHERE p.id = %s
                            '''

GET_NOTES_FOR_ALL_APPOINTMENTS ='''SELECT Content, Date as AppDate, (m.firstName || ' ' || m.lastName) as Author, st.name as Role
                          FROM patient p
                                JOIN Appointment a ON (a.patientid= p.id)
                                JOIN Note N ON (a.id=n.appointmentid)
                                JOIN MedicalStaff m ON (m.id=n.authorid)
                                JOIN StaffType st on (st.id=m.stafftypeid)
                          WHERE p.id =%s
                          ORDER BY AppDate
                        '''

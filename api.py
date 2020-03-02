import queries


class API:
    def __init__(self, db):
        self.db = db

    def getEmployees(self):
        with self.db.connection.cursor() as cursor:
            # Read a single record
            cursor.execute(queries.GET_EMPLOYEES)
            for row in cursor:
                print(row)

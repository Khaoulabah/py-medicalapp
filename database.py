import pymysql


class Database:
    def __init__(self):
        self.connection = pymysql.connect(host='sqleaders-db.cpexrlysbb62.us-east-1.rds.amazonaws.com',
                                          user='admin',
                                          password='sqleaders',
                                          db='medicalapp')

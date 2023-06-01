import mysql.connector
class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute_queryone(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def execute_insert(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        
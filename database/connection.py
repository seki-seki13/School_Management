import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "Alina_Kopbayeva_CS5_16872239"
        self.__password = "C0ventryCUC"
        self.__database = "School_Management_Database"

        self.connection = None

    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                database = self.__database
            )

            if self.connection.is_connected():
                print('Connected')
                return self.connection
        except Error as e:
            print(f'Error connection to MySQL: [{e}]')
            return None

    def close_conn(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('MySQL connection closed')

# obj=DatabaseConnection()
# obj.connect()
# obj.close_conn()
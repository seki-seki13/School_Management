import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    """
    This class manages the connection to the MySQL database
    It utilises Encapsulation to protect sensitive connection details
    """
    def __init__(self):
        # you might need to change these details
        self.__host = "localhost"
        self.__user = "Alina_Kopbayeva_CS5_16872239"
        self.__password = "C0ventryCUC"

        # connects to an existing database created beforehand
        self.__database = "School_Management_System"

        # attribute to store the active connection object
        self.connection = None

    def connect(self):
        """
        A method for attempting tp establish a connection to a database
        Includes try-except exception handling with user-friendly
        error messages
        Returns the connection object if successfully connected
        """
        try:
            self.connection=mysql.connector.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                database = self.__database
            )

            if self.connection.is_connected():
                return self.connection
        except Error as e:
            print(f'Error connection to MySQL: [{e}]')
            return None

    def close_conn(self):
        """
        Closes the connection if it is active
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
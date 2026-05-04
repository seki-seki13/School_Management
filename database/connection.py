from functools import wraps
import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "Alina_Kopbayeva_CS5_16872239"
        self.__password = "C0ventryCUC"
        self.__database = "School_Management_System"

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

def transaction(dictionary=True):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            conn = self.database_manager.connect()
            if not conn:
                return None
            cursor = conn.cursor(dictionary=dictionary)
            try:
                result = func(self, cursor, conn, *args, **kwargs)
                conn.commit()
                print(f'Operation: [{func.__name__} successful.]')
                return result
            except Error as e:
                conn.rollback()
                print(f'Database transaction error: {e}')
                return None
            finally:
                cursor.close()
                self.database_manager.close_conn()
        return wrapper
    return decorator


# obj = DatabaseConnection()
# obj.connect()
# obj.close_conn()
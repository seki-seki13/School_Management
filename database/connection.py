import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

# Load .env from the directory containing this file
load_dotenv(Path(__file__).resolve().parent / ".env")


class DatabaseConnection:
    """
    Manages the connection to the MySQL database.
    """

    def __init__(self):
        self.__host = os.getenv("DB_HOST")
        self.__user = os.getenv("DB_USER")
        self.__password = os.getenv("DB_PASSWORD")
        self.__database = os.getenv("DB_NAME")

        self.connection = None

    def connect(self):
        """Establishes a connection to the database."""
        try:
            # Check configuration before attempting to connect
            if not all([
                self.__host,
                self.__user,
                self.__password,
                self.__database
            ]):
                raise ValueError("Missing database configuration in .env")

            self.connection = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )

            if self.connection.is_connected():
                return self.connection

        except (Error, ValueError) as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def close_conn(self):
        """Closes the connection if it is active."""
        if self.connection and self.connection.is_connected():
            self.connection.close()

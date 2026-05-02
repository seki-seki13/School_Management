from abc import ABC, abstractmethod
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(
    host="localhost",
    user="Alina_Kopbayeva_CS5_16872239",
    password="C0ventryCUC",
    database="School_Management_Database"
)
cursor = conn.cursor()




cursor.close()
conn.close()

























































































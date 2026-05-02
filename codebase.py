import mysql
from mysql import connector
from mysql.connector import errorcode

DB_NAME = "MY_SCHOOL_DATABASE"  # USE YOUR OWN DATABASE NAME HERE

"""

For more information 
https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

"""

# Connect to the database engine
connection = mysql.connector.connect(user='root', password='C0ventryCUC')
cursor = connection.cursor()

"""
A single MySQL server can manage multiple databases.
Typically, you specify the database to switch to when connecting to the MySQL server.
This example does not connect to the database upon connection, so that it can make sure the database exists,
and create it if not:

"""


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


"""
We first try to change to a particular database using the database property of the connection object connection.
If there is an error, we examine the error number to check if the database does not exist.
If so, we call the create_database function to create it for us.

On any other error, the application exits and displays the error message.

"""

try:
    cursor.execute("USE {}".format(DB_NAME))

except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        connection.database = DB_NAME
    else:
        print(err)
        exit(1)


class Student:

    def __init__(self, StudentID, StudentName):
        self.StudentID = StudentID
        self.StudentName = StudentName

    def print_student_details(self):
        print('Student Id:', self.StudentID, ', Student Name:', self.StudentName)

    def print_all_students_details(cursor, connection):
        pass

    def add_new_student(self, cursor, connection):
        cursor.execute(
            f"INSERT INTO StudentsCoursesRegistrations (StudentID, StudentName) VALUES ({self.StudentID}, '{self.StudentName}')")
        connection.commit()
        print('Student Added Successfully')

    def update_student(self, cursor, connection):
        cursor.execute(
            f"UPDATE StudentsCoursesRegistrations SET StudentName = '{self.StudentName}' WHERE StudentID = {self.StudentID}")
        connection.commit()
        print('Student Updated Successfully')

    def delete_student(StudentID, cursor, connection):
        cursor.execute(f"DELETE FROM StudentsCoursesRegistrations WHERE StudentID = {StudentID}")
        connection.commit()
        print('Student Deleted Successfully')


def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS StudentsCoursesRegistrations (
						StudentID	INTEGER PRIMARY KEY,
						StudentName	TEXT,
						CourseID	INTEGER,
						Course_Details	TEXT,
						TeacherID	INTEGER,
						Teacher_name	TEXT,
						Registration_Date	TEXT)''')
    connection.commit()


def main_menu():
    print(
        'what would you like to manage:\n press 1 for Students,\n 2 for teachers,\n 3 for courses,\n 4 for enrollment')
    choice = input('Input your choice: ')
    print(
            '\n\nYou have chosen Student Management,\n press 1 to add a new student,\n 2 to update an exsiting student,\n 3 to delete a student,\n 4 to view all students details')
    student_management_choice = input('Input your choice: ')
    if student_management_choice == '1':
        StudentID = input('input student id: ')
        StudentName = input('input student name: ')
        s = Student(StudentID, StudentName)
        s.add_new_student(cursor, connection)
        s.print_student_details()

    elif student_management_choice == '2':
        StudentID = input(
            'Which student detail you want to update: input student id: ')
        StudentName = input('input an updated student name: ')
        s = Student(StudentID, StudentName)
        s.update_student(cursor, connection)
        s.print_student_details()

    elif student_management_choice == '3':
        Student.delete_student(1, cursor, connection)

    elif student_management_choice == '4':
        Student.print_all_students_details(cursor, connection)

    else:
        if choice == '1':
            print('input is not valid')


create_tables()
main_menu()
connection.close()

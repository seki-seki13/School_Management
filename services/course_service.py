# Importing model, database elements and decorators
from models.course import Course
from database.connection import DatabaseConnection
from utilities.decorators import transaction, sorted_by


class CoursesService:
    """
    Service layer for managing courses records.
    Handles the execution of stored procedures related to the
    Courses table and maps results into the corresponding model.

    CRUD: full CRUD (R4).
    """
    def __init__(self):
        # Initialise the database manager for transaction handling
        self.database_manager = DatabaseConnection()

    # Sorting the loaded data by course ID (R5)
    @sorted_by('course_id')
    @transaction(dictionary=True)
    def view_courses(self, cursor, conn):
        """
        Execute 'v_courses' stored procedure to get all courses
        records for administrative management.
        """
        cursor.callproc('v_courses')
        courses = []

        # Iterate through the stored procedure results
        for result in cursor.stored_results():
            for row in result.fetchall():
                # Instantiating the model
                course = Course(
                    course_id=row['course_id'],
                    course_name=row['course_name']
                )
                courses.append(course)
        return courses


    # Creating a new course (R4)
    @transaction(dictionary=False)
    def add_course(self, cursor, conn, c_id, c_name):
        """
        Execute 'add_course' stored procedure to create a new
        course.
        """
        # Collect parameters into a tuple for the stored procedure call
        new_course = (c_id, c_name)
        cursor.callproc('add_course', new_course)


    # Updating course name (R4)
    @transaction(dictionary=False)
    def update_course(self, cursor, conn, c_id, c_name):
        """
        Execute 'update_course' stored procedure to
        update course name.
        """
        # Collect parameters into a tuple for the stored procedure call
        updated = (c_id, c_name)
        cursor.callproc('update_course', updated)


    #  Deleting a course (R4)
    @transaction(dictionary=False)
    def delete_course(self, cursor, conn, c_id):
        """
        Execute 'delete_course' stored procedure to delete an entity
        with course ID.
        """
        cursor.callproc('delete_course', (c_id,))
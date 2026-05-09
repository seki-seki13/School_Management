"""
Course Model - Represents a course in the system
Inherits validation from BaseModel (demonstrating inheritance and polymorphism)
"""

from models.trying_polymorp.base import BaseModel


class Course(BaseModel):
    """
    Course class with validation.
    """

    def __init__(self, course_id, course_name):
        """
        Initialize a course with validated data.

        Args:
            course_id: Course ID (e.g., 'CS101')
            course_name: Name of the course
        """
        # Use validation methods from BaseModel (polymorphism in action)
        self.course_id = self.validate_string(course_id, 'Course ID', min_length=2, max_length=15)
        self.course_name = self.validate_string(course_name, 'Course name', min_length=3, max_length=50)

    def __str__(self):
        """String representation of course"""
        return f"{self.course_id}: {self.course_name}"
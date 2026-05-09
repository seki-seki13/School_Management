
from services.teacher_service import TeacherService
from utilities.display import DisplayUtils


class TeacherMenu:
    def __init__(self):
        self.teacher_service = TeacherService()

    def view_all_teachers(self):
        try:
            teachers = self.teacher_service.view_all_teachers()
            DisplayUtils.print_teachers(teachers)  # ← Use display here
        except Exception as e:
            DisplayUtils.print_error(f"Error: {e}")

obg = TeacherMenu()
obg.view_all_teachers()
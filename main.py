from services.student_service import StudentService
from services.teacher_service import TeacherService
from services.admin_services import AdminService
from services.room_service import RoomService
from services.course_service import CoursesService

# def test_stud_service():
#     service = StudentService()
#
#     print('1. adding: ')
#     service.add_student('Liu', 'Bai', '2000-01-30',
#                         'Astana', 'Street 123', '+71231212313',
#                         'bai@gmail.com')
#
#     print('\n2. view')
#     service.view_all_students()
#
#     print('\n3. update')
#     service.update_student(1, 'bai6', 'Bai', '2001-02-27',
#                            'Almaty', 'Street 321', '+71231212121',
#                            'bai6@.gmail.com')
#
#     print('\n4. deleting')
#     service.delete_student(2)
#
# def test_teacher_service():
#     t_serv= TeacherService()

    # print('1. addition')
    # t_serv.add_teacher('dokja', 'kim', '1991-02-15',
    #                    'Seul', 'street 456', '+71234567890',
    #                    'demonkingofsalvation@gmail.com')

    # print('\n2. viewing')
    # t_serv.view_all_teachers()

    # print('\n3. updating')
    # t_serv.update_teacher(1, 'oldest', 'dream', '2000-01-01',
    #                       'nowhere', 'no street', '+71234567890',
    #                       'oldestdream@whatever.com')

    # print('\n4. deleting')
    # t_serv.delete_teacher(1)

# def test_admin_serv():
#     ad_serv = Admin_service()
#
#     print('1. add admin')
#     ad_serv.add_admin('Alina', 'Kopbayeva', '2007-11-19',
#                       'Astana', 'Street 123', '+71234567890',
#                       'a.kopbayeva.stu@coventry.edu.kz')
#     print('\n2. view admins')
#     ad_serv.view_all_admins()

# def test_room_serv():
#     r_serv = RoomService()
#
#     print('1. add types')
#     # r_serv.add_room_type('Laboratory')
#     # r_serv.add_room_type('Sports')
#     # r_serv.add_room_type('Lecture')
#
#     print('\n2. add rooms')
#     r_serv.add_room('101', 1, 14, 1)
#     r_serv.add_room('102', 1, 25, 3)
#     r_serv.add_room('201', 2, 50, 2)
#
#     print('\n3. view types')
#     r_serv.v_room_types()
#
#     print('\n4. view rooms')
#     r_serv.view_rooms()

# def test_course_serv():
#     c_serv = CoursesService()

    # print('1. add course')
    # c_serv.add_course('001ALG', 'Algebra')
    # c_serv.add_course('002ENG', 'English Language')
    # c_serv.add_course('003LIT', 'Literature')
    # c_serv.add_course('004CHE', 'Chemistry')
    # c_serv.add_course('005PHE', 'Physical Exersice')
    # c_serv.add_course('000000', 'for deletion')

    # print('\n2. view')
    # c_serv.view_courses()
    #
    # print('\n3. update')
    # c_serv.update_course('005PHE', 'Physical Education')
    #
    # print('\n4. delete')
    # c_serv.delete_course('000000')

if __name__ == '__main__':
    pass
    # test_stud_service()
    # test_teacher_service()
    # test_admin_serv()
    # test_room_serv()
    # test_course_serv()
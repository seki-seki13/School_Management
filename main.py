from services.student_service import StudentService
from services.teacher_service import TeacherService
from services.admin_services import Admin_service

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

def test_admin_serv():
    ad_serv = Admin_service()

    print('1. add admin')
    ad_serv.add_admin('Alina', 'Kopbayeva', '2007-11-19',
                      'Astana', 'Street 123', '+71234567890',
                      'a.kopbayeva.stu@coventry.edu.kz')
    print('\n2. view admins')
    ad_serv.view_all_admins()

if __name__ == '__main__':
    # test_stud_service()
    # test_teacher_service()
    test_admin_serv()

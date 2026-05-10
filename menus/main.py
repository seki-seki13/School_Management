import sys
from services.auth_service import AuthService
from menus.student_menu import run_stud_menu

def main():
    auth = AuthService()

    while True:
        print(f"\n{'='*40}")
        print(' SCHOOL MANAGEMENT SYSTEM LOGIN')
        print(f"{'='*40}\n")
        try:
            username = input('Username: ').strip()
            password = input('Password: ').strip()

            session = auth.login(username, password)

            if session:
                if session.role == 'Student':
                    print('Loading Student Menu...')
                    run_stud_menu(session)
                elif session.role == 'Teacher':
                    print('Loading Teacher Menu...')
                    pass
                elif session.role == 'Admin':
                    print('Loading Admin Menu...')
                    pass
            else:
                ask_again = input('\nLogin failed.\nTry again?\n1. Yes\n2. No\n')
                if ask_again != '1' or ask_again.lower() != 'yes':
                    print('Program exited.')
                    sys.exit()
        except KeyboardInterrupt:
            print('Interrupted from keyboard. Program exited')
            sys.exit()

        except Exception as e:
            print(f'Exception: [{e}]')


if __name__ == '__main__':
    main()

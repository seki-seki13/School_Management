import sys
# Importing the logic for authentication and role-based menus
from services.auth_service import AuthService
from student import run_stud_menu
from admin.admin import run_admin
from teacher import run_teach_menu


def main():
    """
    Main function and the system's entry point.
    Handles the authentication loop,
    directs users to appropriate menus.

    Login details (Use these for the first entry):
    username: alinaadmin
    password: alina123456789

    For easier program operation checking all other logins are:
    1. username = person name (e.g. Aisha)
    2. password = (person name)x3 (e.g. AishaAishaAisha)

    R9: Loop implemented for continuous program execution
    unless the user decides to quit
    """
    auth = AuthService()

    while True:
        print(f"\n{'='*40}")
        print(' SCHOOL MANAGEMENT SYSTEM LOGIN')
        print(f"{'='*40}\n")
        try:
            # Use strip() to remove spaces from the input
            username = input('Username: ').strip()
            password = input('Password: ').strip()

            # Attempt to authenticate the user
            session = auth.login(username, password)

            if session:
                # Role-based authorisation routes to the correct menu
                if session.role == 'Student':
                    print('Loading Student Menu...')
                    run_stud_menu(session)
                elif session.role == 'Teacher':
                    print('Loading Teacher Menu...')
                    run_teach_menu(session)
                elif session.role == 'Admin':
                    print('Loading Admin Menu...')
                    run_admin(session)
            else:
                # Failed login handling
                ask_again = input('\nLogin failed.\nTry again?(y/n): ')
                if ask_again.lower() != 'y':
                    print('Program exited.')
                    sys.exit()

        # Exceptions handling
        except KeyboardInterrupt:
            print('Interrupted from keyboard. Program exited.')
            sys.exit()

        except Exception as e:
            print(f"Invalid input or Error: {e}")


if __name__ == '__main__':
    # Execute the main loop function
    main()